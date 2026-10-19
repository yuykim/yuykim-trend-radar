import { useState } from 'react';
import { formatTime, useTopic } from '../api/client';
import type { Candidate, DashboardPayload, Trend } from '../api/types';

interface Props {
  data: DashboardPayload;
  saved: string[];
  onSave: (id: string) => void;
  onSelect: (id: string, candidate?: Candidate) => void;
  savedOnly?: boolean;
}
const groups = [
  { id: 'research', title: '현재 연구 관심', subtitle: '최근 28일 unique 논문 · 고정 coverage 내 비중' },
  { id: 'new', title: '새 기술 후보', subtitle: '새롭게 포착 · 신규성은 검토 중' },
  { id: 'growth', title: '향후 성장 관찰 후보', subtitle: 'feature와 불확실성을 함께 확인' },
  { id: 'community', title: '커뮤니티 논의', subtitle: '관심의 크기와 연구 성과는 별개' },
];
const candidateKinds = { new_term: '신규 용어', new_cluster: '신규 군집', new_combination: '새 조합', rename_or_alias: '이름 변경·동의어 검토' };

const errorLabels: Record<string, string> = { http_429: '요청 한도 초과 · http_429', config_disabled: '설정에서 비활성 · config_disabled', network: '네트워크 오류 · network' };
const errorLabel = (code: string) => errorLabels[code] ?? code;
function TrendMetric({ trend }: { trend: Trend }) {
  if (trend.support === 'missing') return <div className="metric uncertainty">수집 누락 (missing) · 관심 하락 아님</div>;
  return <div className="metric"><strong>{trend.count_28d}건</strong> 논문 / 28일
    <br />연구 비중 {trend.share_28d === null ? '미확인' : `${(trend.share_28d * 100).toFixed(1)}%`}
    <br />직전 28일 대비 {trend.share_change === null ? '비교 불가' : `${trend.share_change > 0 ? '+' : ''}${(trend.share_change * 100).toFixed(1)} percentage points`}
    {trend.support === 'low_support' && <p className="uncertainty">표본 부족 · low_support · 변화 해석 주의</p>}
    <div className="card-meta">coverage: {trend.coverage_id ?? '미확인'}</div>
  </div>;
}
function TopicCard({ id, trend, candidate, group, index, saved, onSave, onSelect, query }: {
  id: string; trend?: Trend; candidate?: Candidate; group: string; index: number; saved: boolean;
  onSave: Props['onSave']; onSelect: Props['onSelect']; query: string;
}) {
  const { data, error } = useTopic(id);
  const label = data?.label ?? id;
  const text = [label, id, ...(data?.aliases ?? []), ...(candidate?.reasons ?? [])].join(' ').toLocaleLowerCase();
  if (query && !text.includes(query.toLocaleLowerCase())) return null;
  return <article className="card" aria-label={label}>
    <div className="card-header"><span className="tag">{candidate ? candidateKinds[candidate.kind] : '연구 관심'}</span><span className="card-index">FIELD / {String(index + 1).padStart(2, '0')}</span></div>
    <h3 className="card-title"><button className="card-open" aria-label={`${label} 상세 보기`} onClick={() => onSelect(id, candidate)}>{label} <span aria-hidden="true" className="muted">↗</span></button></h3>
    <p className="card-description">{error ?? (candidate ? candidate.reasons.join(' ') : '같은 coverage의 논문 수와 비중을 관찰합니다. 기술의 미래 성공률을 뜻하지 않습니다.')}</p>
    <div className="card-bottom">{trend ? <TrendMetric trend={trend} /> : <div className="metric">최초 관측 {formatTime(candidate!.first_seen_at)}<br />검토 상태: {candidate!.review_status}<br />{group === 'growth' ? '확산 근거·재현 조건 추가 확인 필요' : '새로 수집된 후보 · 새 기술로 확정되지 않음'}</div>}
      <button className="save-small" aria-label={`${label} 관심 ${saved ? '해제' : '저장'}`} aria-pressed={saved} onClick={() => onSave(id)}>{saved ? '★' : '☆'}</button>
    </div>
    <div className="card-meta">{(candidate?.evidence_ids ?? trend?.evidence_ids ?? []).length}개 근거 · 상세에서 출처·기준 시각 확인</div>
  </article>;
}

export function Dashboard({ data, saved, onSave, onSelect, savedOnly = false }: Props) {
  const [query, setQuery] = useState('');
  const [filter, setFilter] = useState('all');
  const candidates = [data.candidates, data.growth_watchlist, data.community_candidates];
  const sources = [...new Set(data.source_runs.map(run => run.source))];
  const allMissing = data.trends.length > 0 && data.trends.every(t => t.support === 'missing');
  const degraded = data.source_runs.filter(run => run.status === 'partial' || run.status === 'failed');
  return <>
    <section className="toolbar" aria-label="기술 탐색">
      <label className="search"><span aria-hidden="true">⌕</span><input type="search" aria-label="기술 이름 또는 키워드 검색" placeholder="기술 이름 또는 키워드 검색" value={query} onChange={e => setQuery(e.target.value)} /></label>
      <div className="filters" aria-label="분류 필터">{[{ id: 'all', title: '전체' }, ...groups].map(g => <button key={g.id} className={filter === g.id ? 'active' : ''} aria-pressed={filter === g.id} onClick={() => setFilter(g.id)}>{g.title}</button>)}</div>
    </section>
    {allMissing && !savedOnly && <p className="uncertainty" role="note">이번 기준 시각에는 논문 수를 표시하지 않습니다. {degraded.length ? `${degraded.map(r => `${r.source} ${r.status === 'partial' ? '일부 수집' : '수집 실패'}${r.error_code ? ` (${errorLabel(r.error_code)})` : ''}`).join(', ')} 때문에 coverage가 완전하지 않습니다.` : '같은 coverage의 분모를 확보하지 못했습니다.'} 다음 실행에서 이어서 수집합니다.</p>}
    {savedOnly && <p className="saved-intro">관심 기술 {saved.length}개 · 이 브라우저에 저장됩니다.</p>}
    <div className="results">
      {groups.map((group, groupIndex) => {
        if (filter !== 'all' && filter !== group.id) return null;
        const items = groupIndex === 0 ? data.trends.map(t => ({ id: t.entity_id, trend: t, candidate: undefined })) : candidates[groupIndex - 1].map(c => ({ id: c.entity_id, candidate: c, trend: undefined }));
        const visible = items.filter(item => !savedOnly || saved.includes(item.id));
        return <section className="section" key={group.id}><div className="section-heading"><h2><span className="section-number">0{groupIndex + 1}</span>{group.title}</h2><span className="section-subtitle">{group.subtitle}</span></div>
          <div className="grid">{visible.map((item, i) => <TopicCard {...item} key={item.candidate?.id ?? item.id} group={group.id} index={i} saved={saved.includes(item.id)} onSave={onSave} onSelect={onSelect} query={query.trim()} />)}</div>
          {!visible.length && <p className="empty">{savedOnly ? '이 영역에 저장한 관심 기술이 없습니다.' : '아직 표시할 자료가 없습니다.'}</p>}
        </section>;
      })}
      <div className="empty no-results"><h2>일치하는 기술이 없습니다.</h2><p>검색어 또는 분류 필터를 바꿔보세요.</p><button onClick={() => { setQuery(''); setFilter('all'); }}>검색 · 필터 초기화</button></div>
    </div>
    <p className="summary-note">표본 5건 미만은 low_support입니다. source 장애와 coverage 변경 기간은 관심 하락으로 해석하지 않습니다. 커뮤니티 표본 부족은 관심 부재를 뜻하지 않습니다.</p>
    <section className="section source-status" aria-label="수집 상태"><h2>수집 상태와 기준 시각</h2><p>기준 시각: {formatTime(data.as_of)} · 매일 07:00 Asia/Seoul 갱신</p>
      {sources.length === 0 && <p>수집 기록이 없습니다. 초기 데이터 부족으로 관심을 판단할 수 없습니다.</p>}
      {sources.map(source => {
        const runs = data.source_runs.filter(run => run.source === source).sort((a, b) => b.started_at.localeCompare(a.started_at));
        const latest = runs[0];
        const success = runs.find(run => run.status === 'ok');
        const status = { ok: '정상', partial: '일부 수집 · 누락 있음', failed: '수집 실패', disabled: '비활성 · 미수집' }[latest.status];
        return <div className="source-row" key={source}><strong>{source}: {status}</strong><span>최근 시도 {formatTime(latest.started_at)}</span><span>마지막 정상 결과: {success ? formatTime(success.finished_at) : '확인 불가'}</span><small>coverage: {latest.coverage_id ?? '미확인'}{latest.error_code ? ` · ${errorLabel(latest.error_code)}` : ''}</small></div>;
      })}
    </section>
  </>;
}
