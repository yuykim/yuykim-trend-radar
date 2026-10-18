import { useState } from 'react';
import { formatTime, safeUrl, useTopic } from '../api/client';
import type { Candidate, CandidateSummary, Document, Review, TopicDetail as TopicData } from '../api/types';

interface Props {
  id: string;
  asOf?: string;
  candidate?: Candidate;
  review?: Review;
  onReview?: (review: Review) => void;
  saved?: boolean;
  onSave?: (id: string) => void;
}
const reviewLabels = { already_known: '이미 알고 있었나요?', relevant: '관심 분야와 관련 있나요?', distinct: '기존 기술과 차이가 있나요?', useful: '유용했나요?' };
function ReviewForm({ candidate, review, onReview }: { candidate: Candidate; review?: Review; onReview: (review: Review) => void }) {
  const [values, setValues] = useState<Record<keyof typeof reviewLabels, string>>(() => Object.fromEntries(Object.keys(reviewLabels).map(key => [key, review?.[key as keyof typeof reviewLabels] == null ? '' : String(review[key as keyof typeof reviewLabels])])) as Record<keyof typeof reviewLabels, string>);
  const [minutes, setMinutes] = useState(review?.minutes_spent?.toString() ?? '');
  const [message, setMessage] = useState('');
  return <form className="review-form" onSubmit={e => {
    e.preventDefault();
    const spent = minutes.trim() === '' ? null : Number(minutes);
    if (spent !== null && (!Number.isFinite(spent) || spent < 0)) { setMessage('검토 시간은 0 이상의 숫자로 입력하세요.'); return; }
    const answer = (key: keyof typeof reviewLabels) => values[key] === '' ? null : values[key] === 'true';
    onReview({ candidate_id: candidate.id, reviewed_at: new Date().toISOString(), already_known: answer('already_known'), relevant: answer('relevant'), distinct: answer('distinct'), useful: answer('useful'), minutes_spent: spent });
    setMessage('리뷰를 반영했습니다. 브라우저 저장 상태를 확인하세요.');
  }}>
    <h3>후보 리뷰</h3><p>모르는 항목은 미판단으로 남깁니다. 이 브라우저에 저장되며 JSON으로 내보낼 수 있습니다.</p>
    {Object.entries(reviewLabels).map(([key, label]) => <label key={key}>{label}<select value={values[key as keyof typeof reviewLabels]} onChange={e => setValues({ ...values, [key]: e.target.value })}><option value="">미판단</option><option value="true">예</option><option value="false">아니요</option></select></label>)}
    <label>검토 시간 (분)<input type="number" min="0" step="any" value={minutes} onChange={e => setMinutes(e.target.value)} /></label>
    <button className="detail-save" type="submit">리뷰 저장</button><p role="status">{message}</p>
  </form>;
}
function Summary({ summary, documents }: { summary: CandidateSummary | null; documents: Document[] }) {
  if (!summary) return <p className="summary-note">LLM 요약이 없습니다. 원문과 아래 규칙 설명으로 검토할 수 있습니다.</p>;
  return <section className="detail-section"><h3>무엇이 새로 달라졌나요?</h3><p className="tag">LLM 생성, 원문 확인 필요</p><p>{summary.why_new}</p><h3>이전 접근과의 차이</h3><p>{summary.difference}</p>
    <p className="card-meta">model: {summary.model} · 생성 시각: {formatTime(summary.generated_at)}</p>
    <ul>{summary.source_document_ids.map(id => {
      const doc = documents.find(d => d.id === id);
      const href = doc && safeUrl(doc.url);
      return <li key={id}>{href ? <a href={href} target="_blank" rel="noreferrer">요약 출처: {doc.title}</a> : `요약 출처 ${id}: 원문 연결 미확인`}</li>;
    })}</ul>
    <ul className="uncertainty">{summary.limitations.map((text, i) => <li key={i}>{text}</li>)}</ul>
  </section>;
}
const documentStatus = { preprint: 'preprint · 동료심사 전', accepted: 'accepted · 게재 승인', retracted: 'retracted · 철회됨', unknown: 'unknown · 동료심사 상태 미확인' };
function Content({ data, ...props }: Props & { data: TopicData }) {
  return <>
    <p className="tag">TECHNOLOGY BRIEF</p><h2 id="detail-title">{data.label}</h2>
    <p className="detail-lead">{data.aliases.length ? `다른 이름: ${data.aliases.join(', ')}` : '확인된 다른 이름 없음'}</p>
    <p>기준 시각: {props.asOf ? formatTime(props.asOf) : 'dashboard 기준 시각 미제공'}</p>
    {props.onSave && <button className="detail-save" aria-pressed={props.saved ?? false} onClick={() => props.onSave!(props.id)}>{props.saved ? '★ 관심 저장됨' : '☆ 관심 저장'}</button>}
    <Summary summary={data.summary ?? props.candidate?.summary ?? null} documents={data.documents} />
    <section className="detail-section"><h3>규칙 기반 후보 설명</h3>{props.candidate ? <><p>발견 경로: {props.candidate.kind} · 검토 상태: {props.candidate.review_status}</p><p>최초 관측: {formatTime(props.candidate.first_seen_at)}</p><ul>{props.candidate.reasons.map((r, i) => <li key={i}>{r}</li>)}</ul><p>새로 수집된 이름·군집·조합은 검토 후보입니다. 동명이의어나 기존 기술의 이름 변경일 수 있습니다.</p></> : <p>고정 coverage 내 최근 28일 unique 논문 비중을 관찰합니다. 표본 부족과 coverage 변경 시 직접 비교하지 않습니다.</p>}</section>
    <section className="detail-section"><h3>연구 관심과 관측값</h3>
      {!data.observations.length && <p>초기 데이터 부족 · 관측값이 없습니다.</p>}
      {data.observations.map((o, index) => <div className="evidence" key={index}><strong>{o.metric}: {o.state === 'missing' ? '수집 누락 (missing)' : o.state === 'unknown' || o.value === null ? '미확인 (unknown)' : o.value}</strong><p>source: {o.source} · coverage: {o.coverage_id}</p><p>이용 가능 시각: {formatTime(o.available_at)}<br />관측 시각: {formatTime(o.observed_at)}</p></div>)}
      <p>동일 metric의 시계열이 충분히 쌓이기 전에는 추이를 만들지 않습니다. 코드·모델 공개와 독립 연구기관 수는 근거가 있을 때만 판단합니다.</p>
    </section>
    <section className="detail-section"><h3>대표 근거</h3>
      {!data.documents.length && <p>연결된 문헌이 없습니다. 근거를 확인할 수 없습니다.</p>}
      {data.documents.map(doc => <article className="evidence" key={doc.id} id={`document-${doc.id}`}><span className="tag">{documentStatus[doc.status]}</span><h3>{safeUrl(doc.url) ? <a href={safeUrl(doc.url)} target="_blank" rel="noreferrer">{doc.title}</a> : doc.title}</h3><p>{doc.abstract ?? '초록 미확인'}</p><p className="uncertainty">초록 기반 · 본문 확인 안 됨</p><p>source: {doc.source} · 버전: {doc.version ?? '미확인'}</p><p>버전 공개: {formatTime(doc.published_at)}<br />최초 공개: {formatTime(doc.first_public_at)}<br />관측 시각: {formatTime(doc.observed_at)}<br />이용 가능 시각: {formatTime(doc.available_at)}</p><p>동료심사 상태와 본문·실험 조건 검증은 별개입니다.</p></article>)}
    </section>
    <section className="detail-section"><h3>관계 근거</h3>{!data.evidence_edges.length && <p>확인할 관계 근거가 없습니다.</p>}{data.evidence_edges.map(edge => <article className="evidence" key={edge.id}><strong>{edge.source_id} → {edge.target_id} · {edge.relation}</strong><p>검토 상태: {edge.review_status} · 이용 가능 시각: {formatTime(edge.available_at)}</p><p>{safeUrl(edge.evidence_url) ? <a href={safeUrl(edge.evidence_url)} target="_blank" rel="noreferrer">관계 출처</a> : '출처 URL 미확인'} · 위치: {edge.evidence_location ?? '미확인'}</p></article>)}</section>
    <section className="detail-section"><h3>아직 확인할 것</h3><ul className="uncertainty">{data.limitations.map((text, i) => <li key={i}>{text}</li>)}</ul></section>
    <details className="disclosure"><summary>기업 · 주가 보조 정보</summary><p>검증된 기업·증권 연결과 시세가 없습니다. 수익률 상관과 기술 관계는 별도로 다룹니다.</p></details>
    {props.candidate && props.onReview && <section className="detail-section"><ReviewForm key={props.candidate.id} candidate={props.candidate} review={props.review} onReview={props.onReview} /></section>}
  </>;
}
export function TopicDetail(props: Props) {
  const { data, error } = useTopic(props.id);
  if (error) return <p role="alert">{error}</p>;
  if (!data) return <p role="status">상세 자료를 불러오는 중…</p>;
  return <Content {...props} data={data} />;
}
export default TopicDetail;
