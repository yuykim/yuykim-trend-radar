import type { GraphPayload } from '../api/types';

export const COMPANY_ZOOM = 1.2;
export const MAX_VISIBLE_NODES = 500;

/** Wire relation names stay intact; correlation is never recast as a technology relation. */
export function isCorrelation(relation: string): boolean {
  return relation === 'correlation' || relation === 'stock_correlation';
}

/** Layers: technology, company, correlation. Unknown node types require their exact type as a layer. */
export function visibleGraph(data: GraphPayload, zoom: number, layers: string[]): GraphPayload {
  const nodes = data.nodes.filter(node => layers.includes(node.type)
    && (node.type !== 'company' || zoom >= COMPANY_ZOOM)).slice(0, MAX_VISIBLE_NODES);
  const ids = new Set(nodes.map(node => node.id));
  return {
    nodes,
    edges: data.edges.filter(edge => ids.has(edge.source_id) && ids.has(edge.target_id)
      && (!isCorrelation(edge.relation) || layers.includes('correlation'))),
    generated_at: data.generated_at,
  };
}
