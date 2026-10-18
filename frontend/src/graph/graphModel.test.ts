import { describe, expect, it } from 'vitest';
import type { EvidenceEdge, GraphPayload } from '../api/types';
import { visibleGraph } from './graphModel';

const edge = (id: string, source_id: string, target_id: string, relation = 'builds_on'): EvidenceEdge => ({
  id, source_id, target_id, relation, evidence_url: 'https://example.org/paper',
  evidence_location: 'section 2', available_at: null, review_status: 'proposed',
});
const data: GraphPayload = {
  nodes: [{ id: 'tech', label: 'World Models', type: 'technology' },
    { id: 'a', label: 'A', type: 'company' }, { id: 'b', label: 'B', type: 'company' }],
  edges: [edge('research', 'a', 'tech', 'authored_research'), edge('returns', 'a', 'b', 'correlation')],
  generated_at: '2026-10-17T22:00:00Z',
};

describe('visibleGraph', () => {
  it('test_zoom_reveals_companies', () => {
    expect(visibleGraph(data, 1.19, ['technology', 'company']).nodes.map(n => n.id)).toEqual(['tech']);
    expect(visibleGraph(data, 1.2, ['technology', 'company']).nodes).toEqual(data.nodes);
  });
  it('test_correlation_never_becomes_technology_edge', () => {
    expect(visibleGraph(data, 2, ['technology', 'company']).edges.map(e => e.id)).toEqual(['research']);
    const result = visibleGraph(data, 2, ['company', 'correlation']);
    expect(result.edges).toEqual([data.edges[1]]);
    expect(result.edges[0].relation).toBe('correlation');
    expect(result.edges[0].available_at).toBeNull();
    expect(data.edges[0].relation).toBe('authored_research');
  });
  it('caps nodes at 500 and omits dangling edges without making replacements', () => {
    const large: GraphPayload = { ...data,
      nodes: Array.from({ length: 502 }, (_, i) => ({ id: String(i), label: String(i), type: 'technology' })),
      edges: [edge('ok', '0', '1'), edge('cut', '0', '500'), edge('orphan', '0', 'absent')],
    };
    const result = visibleGraph(large, 1, ['technology']);
    expect(result.nodes).toHaveLength(500);
    expect(result.edges).toEqual([large.edges[0]]);
    expect(large.nodes).toHaveLength(502);
    expect(result.generated_at).toBe(large.generated_at);
  });
  it('supports empty graphs, isolated nodes and disabled layers', () => {
    expect(visibleGraph({ ...data, nodes: [], edges: [] }, 1, ['technology']).nodes).toEqual([]);
    expect(visibleGraph(data, 1, ['technology']).edges).toEqual([]);
    expect(visibleGraph(data, 2, []).nodes).toEqual([]);
  });
  it('keeps stock_correlation on its own layer and preserves unknown relation names', () => {
    const stock = edge('stock', 'a', 'b', 'stock_correlation');
    const unknown = edge('unknown', 'a', 'b', 'unclassified');
    const payload = { ...data, edges: [stock, unknown] };
    expect(visibleGraph(payload, 2, ['company']).edges).toEqual([unknown]);
    expect(visibleGraph(payload, 2, ['company', 'correlation']).edges).toEqual([stock, unknown]);
  });
});
