/** Site-data contract. IDs are opaque strings; timestamps are ISO 8601 UTC. */
export type Timestamp = string;
export type ReviewStatus = 'proposed' | 'verified' | 'rejected';

export interface Document {
  id: string;
  source: string;
  source_id: string;
  canonical_id: string;
  title: string;
  abstract: string | null;
  url: string;
  version: string | null;
  published_at: Timestamp | null;
  first_public_at: Timestamp | null;
  observed_at: Timestamp;
  available_at: Timestamp | null;
  status: 'preprint' | 'accepted' | 'retracted' | 'unknown';
}
export interface Observation {
  entity_id: string;
  metric: string;
  value: number | null;
  available_at: Timestamp | null;
  observed_at: Timestamp;
  source: string;
  coverage_id: string;
  state: 'ok' | 'missing' | 'unknown';
}
export interface EvidenceEdge {
  id: string;
  source_id: string;
  target_id: string;
  relation: string;
  evidence_url: string;
  evidence_location: string | null;
  available_at: Timestamp | null;
  review_status: ReviewStatus;
}
export interface SourceRun {
  source: string;
  started_at: Timestamp;
  finished_at: Timestamp | null;
  status: 'ok' | 'partial' | 'failed' | 'disabled';
  coverage_id: string | null;
  item_count: number;
  error_code: string | null;
}
export interface Trend {
  entity_id: string;
  count_28d: number;
  share_28d: number | null;
  share_change: number | null;
  support: 'ok' | 'low_support' | 'missing';
  coverage_id: string | null;
  evidence_ids: string[];
}
export interface CandidateSummary {
  why_new: string;
  difference: string;
  limitations: string[];
  model: string;
  generated_at: Timestamp;
  source_document_ids: string[];
}
export interface Candidate {
  id: string;
  entity_id: string;
  kind: 'new_term' | 'new_cluster' | 'new_combination' | 'rename_or_alias';
  first_seen_at: Timestamp;
  reasons: string[];
  evidence_ids: string[];
  review_status: ReviewStatus;
  summary: CandidateSummary | null;
}
export interface Review {
  candidate_id: string;
  reviewed_at: Timestamp;
  already_known: boolean | null;
  relevant: boolean | null;
  distinct: boolean | null;
  useful: boolean | null;
  minutes_spent: number | null;
}
export interface GraphNode {
  id: string;
  label: string;
  type: string;
}
export interface GraphPayload {
  nodes: GraphNode[];
  edges: EvidenceEdge[];
  generated_at: Timestamp;
}
export interface DashboardPayload {
  as_of: Timestamp;
  trends: Trend[];
  candidates: Candidate[];
  community_candidates: Candidate[];
  growth_watchlist: Candidate[];
  source_runs: SourceRun[];
}
export interface TopicDetail {
  entity_id: string;
  label: string;
  aliases: string[];
  documents: Document[];
  observations: Observation[];
  evidence_edges: EvidenceEdge[];
  limitations: string[];
  summary: CandidateSummary | null;
}
