// Synthetic, retrospective UI fixtures. This script performs no network calls.
import { mkdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('../public/data/', import.meta.url));
mkdirSync(`${root}/topics`, { recursive: true });
const asOf = '2026-10-17T22:00:00Z';
const write = (path, data) => writeFileSync(`${root}/${path}.json`, JSON.stringify(data, null, 2) + '\n', 'utf8');
const summary = {
  why_new: '데모: 촉각과 시각 표현을 함께 학습하는 조합을 검토합니다.',
  difference: '데모: 시각 중심 접근과 센서 조건을 비교해야 합니다.',
  limitations: ['합성 예시이며 실제 연구 결과가 아닙니다.', '센서 간 전이와 재현성은 미확인입니다.'],
  model: 'demo-not-an-api-call', generated_at: asOf, source_document_ids: ['doc-tactile'],
};
const candidate = {
  id: 'candidate-tactile', entity_id: 'tactile', kind: 'new_combination',
  first_seen_at: '2026-10-12T01:00:00Z',
  reasons: ['데모: seed 외 조합 후보. 이름만으로 신규성을 확정하지 않습니다.'],
  evidence_ids: ['doc-tactile'], review_status: 'proposed', summary,
};
const growth = {
  id: 'candidate-vla', entity_id: 'vla', kind: 'new_cluster', first_seen_at: '2026-10-10T01:00:00Z',
  reasons: ['데모 관찰 feature: 연구 비중 변화.', '독립 연구기관 수, 코드·모델 공개 상태는 미확인입니다.'],
  evidence_ids: ['doc-vla'], review_status: 'proposed', summary: null,
};
const trends = [['world', 12, .24, .04, 'ok'], ['jepa', 0, null, null, 'missing'], ['tactile', 3, .06, null, 'low_support']].map(([entity_id, count_28d, share_28d, share_change, support]) => ({ entity_id, count_28d, share_28d, share_change, support, coverage_id: 'demo-physical-ai-v1', evidence_ids: [`doc-${entity_id}`] }));
const source_runs = [
  { source: 'arxiv', started_at: '2026-10-17T21:55:00Z', finished_at: asOf, status: 'ok', coverage_id: 'demo-physical-ai-v1', item_count: 20, error_code: null },
  { source: 'openreview', started_at: '2026-10-17T21:55:00Z', finished_at: asOf, status: 'failed', coverage_id: 'demo-physical-ai-v1', item_count: 0, error_code: 'demo_timeout' },
  { source: 'openreview', started_at: '2026-10-16T21:55:00Z', finished_at: '2026-10-16T22:00:00Z', status: 'ok', coverage_id: 'demo-physical-ai-v1', item_count: 10, error_code: null },
  { source: 'bluesky', started_at: asOf, finished_at: null, status: 'disabled', coverage_id: null, item_count: 0, error_code: null },
];
write('dashboard', { as_of: asOf, trends, candidates: [candidate], community_candidates: [], growth_watchlist: [growth], source_runs });
const nodes = [['world', 'World Models', 'World Model 데모 문헌'], ['jepa', 'JEPA', 'JEPA 데모 문헌'], ['tactile', 'Tactile Learning', '촉각 학습 데모 문헌'], ['vla', 'VLA', 'VLA 데모 문헌']];
for (const [entity_id, label, title] of nodes) {
  const missing = ['world', 'jepa'].includes(entity_id);
  const doc = {
    id: `doc-${entity_id}`, source: 'demo', source_id: `demo-${entity_id}`, canonical_id: `demo-${entity_id}`,
    title, abstract: '합성 데모 초록입니다. 실제 논문이나 검증된 실험 결과가 아닙니다.', url: `https://example.org/radar/${entity_id}`, version: 'v1',
    published_at: '2026-10-09T00:00:00Z', first_public_at: entity_id === 'jepa' ? null : '2026-10-09T00:00:00Z', observed_at: '2026-10-12T01:00:00Z', available_at: '2026-10-12T01:00:00Z', status: 'preprint',
  };
  write(`topics/${entity_id}`, {
    entity_id, label, aliases: entity_id === 'tactile' ? ['촉각 학습'] : [], documents: [doc],
    observations: [{ entity_id, metric: 'research_share_28d', value: missing ? null : .06, available_at: asOf, observed_at: asOf, source: missing ? 'openreview' : 'demo', coverage_id: 'demo-physical-ai-v1', state: missing ? 'missing' : 'ok' }],
    evidence_edges: entity_id === 'tactile' ? [{ id: 'demo-edge', source_id: 'tactile', target_id: 'vla', relation: 'combines_with', evidence_url: 'https://example.org/radar/tactile', evidence_location: '데모 초록', available_at: '2026-10-12T01:00:00Z', review_status: 'proposed' }] : [],
    limitations: ['DEMO · 합성 데이터. 실제 연구 평가에 사용할 수 없습니다.', '초록만 확인하는 예시이며 본문·코드·모델·재현성은 미확인입니다.'], summary: entity_id === 'tactile' ? summary : null,
  });
}
write('graph', { nodes: nodes.map(([id, label]) => ({ id, label, type: 'technology' })), edges: [], generated_at: asOf });
