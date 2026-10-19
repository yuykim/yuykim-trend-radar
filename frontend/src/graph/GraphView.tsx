import { useEffect, useMemo, useRef, useState } from 'react';
import cytoscape from 'cytoscape';
import type { Core, StylesheetJson } from 'cytoscape';
import type { EvidenceEdge, GraphNode, GraphPayload } from '../api/types';
import { COMPANY_ZOOM, isCorrelation, MAX_VISIBLE_NODES, visibleGraph } from './graphModel';

export interface GraphViewProps {
  data: GraphPayload;
  onSelect: (id: string) => void;
}

const graphStyle: StylesheetJson = [
  { selector: 'node', style: { label: 'data(label)', 'background-color': '#f2f7f2',
    'border-color': '#76a493', 'border-width': 2, color: '#172b3b',
    'font-size': 12, 'text-valign': 'bottom', 'text-margin-y': 8, width: 48, height: 48 } },
  { selector: 'node.company', style: { shape: 'round-rectangle', width: 90, height: 34,
    'background-color': '#f4ede1', 'border-color': '#b79c70' } },
  { selector: 'edge', style: { width: 1.5, 'line-color': '#a6bdb2', 'curve-style': 'bezier',
    label: 'data(relation)', 'font-size': 9, color: '#52685c', 'text-background-color': '#fff',
    'text-background-opacity': 1, 'text-background-padding': '3px' } },
  { selector: 'edge.correlation', style: { 'line-style': 'dashed', 'line-color': '#b38750', color: '#805d30' } },
  { selector: ':selected', style: { 'border-color': '#177b70', 'border-width': 4, 'line-color': '#177b70' } },
];

function sourceUrl(value: string): string | undefined {
  try { const url = new URL(value); return ['https:', 'http:'].includes(url.protocol) ? url.href : undefined; }
  catch { return undefined; }
}

export function GraphView({ data, onSelect }: GraphViewProps) {
  const container = useRef<HTMLDivElement>(null);
  const core = useRef<Core | null>(null);
  const [zoom, setZoom] = useState(1);
  const [layers, setLayers] = useState(['technology', 'company']);
  const [relation, setRelation] = useState('');
  // Snapshot the full evidence at selection time, independently of all visibility filters.
  const [selection, setSelection] = useState<{ node: GraphNode; edges: EvidenceEdge[] } | null>(null);
  const selectRef = useRef<(id: string) => void>(() => {});
  selectRef.current = id => {
    const node = data.nodes.find(item => item.id === id);
    if (!node) return;
    setSelection({ node, edges: data.edges.filter(edge => edge.source_id === id || edge.target_id === id) });
    onSelect(id);
  };
  const eligible = useMemo(() => visibleGraph(data, zoom, layers), [data, zoom, layers]);
  const displayed = useMemo(() => ({ ...eligible,
    edges: eligible.edges.filter(edge => !relation || edge.relation === relation),
  }), [eligible, relation]);
  const relations = Array.from(new Set([...data.edges.map(edge => edge.relation), 'correlation'])).sort();
  const positions = useRef(new Map<string, { x: number; y: number }>());

  useEffect(() => {
    if (!container.current) return;
    const instance = cytoscape({ container: container.current, elements: [], style: graphStyle,
      layout: { name: 'preset' }, minZoom: 0.4, maxZoom: 3, zoom: 1,
      wheelSensitivity: 0.2, boxSelectionEnabled: false, autounselectify: false });
    core.current = instance;
    instance.on('tap', 'node', event => selectRef.current(event.target.data('entityId')));
    instance.on('zoom', () => setZoom(Math.round(instance.zoom() * 1000) / 1000));
    instance.on('dragfree', 'node', event => {
      positions.current.set(event.target.data('entityId'), { ...event.target.position() });
    });
    const observer = typeof ResizeObserver === 'undefined' ? null : new ResizeObserver(() => instance.resize());
    observer?.observe(container.current);
    return () => { observer?.disconnect(); instance.destroy(); core.current = null; };
  }, []);

  useEffect(() => {
    const instance = core.current;
    if (!instance) return;
    // Stable internal IDs avoid collisions between opaque node IDs and edge IDs.
    const nodeIds = new Map(displayed.nodes.map(node => [node.id, `node:${node.id}`]));
    instance.batch(() => {
      instance.elements().remove();
      instance.add(displayed.nodes.map(node => {
        if (!positions.current.has(node.id)) {
          // Allocate unused slots so revealing companies cannot overlap existing technology nodes.
          const index = positions.current.size;
          const columns = 3;
          positions.current.set(node.id, { x: 150 + (index % columns) * 260, y: 75 + Math.floor(index / columns) * 120 });
        }
        return { data: { id: nodeIds.get(node.id), entityId: node.id, label: node.label },
          classes: node.type === 'company' ? 'company' : '', position: positions.current.get(node.id) };
      }));
      instance.add(displayed.edges.map(edge => ({ data: { ...edge, id: `edge:${edge.id}`,
        source: nodeIds.get(edge.source_id), target: nodeIds.get(edge.target_id) },
        classes: isCorrelation(edge.relation) ? 'correlation' : '' })));
      if (selection) instance.getElementById(`node:${selection.node.id}`).select();
    });
  }, [displayed, selection]);

  function changeZoom(delta: number) {
    const next = Math.max(0.4, Math.min(3, Math.round((zoom + delta) * 10) / 10));
    core.current?.zoom(next);
    setZoom(next);
  }
  function toggleLayer(layer: string) {
    setLayers(current => current.includes(layer) ? current.filter(item => item !== layer) : [...current, layer]);
  }
  const eligibleCount = data.nodes.filter(node => layers.includes(node.type)
    && (node.type !== 'company' || zoom >= COMPANY_ZOOM)).length;
  const selectedVisible = selection && displayed.nodes.some(node => node.id === selection.node.id);

  return <section aria-label="기술 관계도">
    <div className="graph-header">
      <p>기술의 관계를 살펴보세요. 기업은 120% 이상 확대하면 표시됩니다.</p>
      <div className="graph-controls">
        <button type="button" aria-label="축소" onClick={() => changeZoom(-0.2)} disabled={zoom <= 0.4} style={{ minHeight: 44 }}>−</button>
        <output aria-label="확대 비율">{Math.round(zoom * 100)}%</output>
        <button type="button" aria-label="확대" onClick={() => changeZoom(0.2)} disabled={zoom >= 3} style={{ minHeight: 44 }}>+</button>
      </div>
    </div>
    <fieldset className="layer-controls" style={{ border: 0, padding: 0 }}>
      <legend>레이어</legend>
      {([['technology', '기술'], ['company', '기업'], ['correlation', '주가 상관']] as const).map(([key, label]) =>
        <label key={key} style={{ minHeight: 44 }}><input type="checkbox" checked={layers.includes(key)} onChange={() => toggleLayer(key)} />{label}</label>)}
      <label>관계 필터 <select value={relation} onChange={event => setRelation(event.target.value)} style={{ minHeight: 44, maxWidth: '100%' }}>
        <option value="">모든 관계</option>
        {relations.map(value => <option key={value} value={value}>{value}</option>)}
      </select></label>
    </fieldset>
    <p role="status" className="graph-note">표시 {displayed.nodes.length} / 전체 {data.nodes.length}개 노드 · {displayed.edges.length}개 관계 · 최대 {MAX_VISIBLE_NODES}개
      {eligibleCount > MAX_VISIBLE_NODES && ` · 상한으로 ${eligibleCount - MAX_VISIBLE_NODES}개 노드 생략`}
      {' · 레이어: '}{layers.join(', ') || '없음'}{' · 관계: '}{relation || '전체'}
    </p>
    <div className="graph-shell" style={{ position: 'relative' }}>
      <div ref={container} role="img" aria-label="기술과 기업 관계 그래프. 아래 노드 목록에서 키보드로 선택할 수 있습니다."
        style={{ height: 'clamp(300px, 55vh, 480px)', width: '100%' }} />
      {!displayed.nodes.length && <p style={{ position: 'absolute', top: '40%', width: '100%', textAlign: 'center' }}>표시할 노드가 없습니다. 레이어를 조정하세요.</p>}
    </div>
    <div className="graph-legend">
      <span>○ 기술</span><span>▭ 기업</span>
      <span><i className="legend-line" />근거가 있는 관계</span>
      <span><i className="legend-line dashed" />주가 상관 · 기술 관계와 별도</span>
    </div>
    <p className="graph-note">생성 시각: {data.generated_at} · 필터·확대·상한으로 생략된 관계가 있습니다. 선이 없다는 것이 관계가 없다는 뜻은 아닙니다.
      주가 상관은 기술 관계·인과관계·미래 수익률을 뜻하지 않습니다. 값이 없는 상관은 추정해 만들지 않습니다.</p>
    <details open><summary>표시된 노드 목록 · 키보드로 선택</summary>
      <ul style={{ maxHeight: 240, overflow: 'auto' }}>{displayed.nodes.map(node => <li key={node.id}>
        <button type="button" aria-label={`${node.label} 선택`} aria-pressed={selection?.node.id === node.id}
          onClick={() => selectRef.current(node.id)} style={{ minHeight: 44, padding: '6px 12px', margin: 3 }}>{node.label}</button>
      </li>)}</ul>
    </details>
    <section aria-label="선택한 노드의 근거" className="evidence">
      {selection ? <>
        <h2>{selection.node.label}</h2>
        {!selectedVisible && <p>현재 화면에서 숨겨진 노드입니다. 선택과 근거는 유지됩니다.</p>}
        <p>노드 ID: {selection.node.id} · {selection.node.type}</p>
        {selection.edges.length ? selection.edges.map(edge => <article key={edge.id} style={{ borderTop: '1px solid var(--border)', paddingBlock: 12 }}>
          <h3>{edge.relation}{isCorrelation(edge.relation) ? ' · 주가 상관' : ''}</h3>
          <p>{edge.source_id} → {edge.target_id}</p>
          {sourceUrl(edge.evidence_url) ? <a href={sourceUrl(edge.evidence_url)} target="_blank" rel="noopener noreferrer">원문 근거</a> : <p>출처 URL unknown</p>}
          <p>{edge.evidence_location ?? '근거 위치 unknown'}</p>
          <p>{edge.available_at ? `시점 ${edge.available_at}` : '시점 unknown'}</p>
          <p>review: {edge.review_status}</p>
        </article>) : <p>제공된 관계 근거가 없습니다. 고립 노드도 표시합니다.</p>}
      </> : <p>노드를 선택하면 출처·시점·검토 상태를 확인할 수 있습니다.</p>}
    </section>
  </section>;
}

export default GraphView;
