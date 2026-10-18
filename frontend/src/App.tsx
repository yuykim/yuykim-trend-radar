import { useEffect, useRef, useState } from 'react';
import { formatTime, getDashboard } from './api/client';
import { exportLocalData, isReviews, isWatchlist, REVIEWS_KEY, useLocalData, WATCHLIST_KEY } from './api/storage';
import type { Candidate, DashboardPayload, Review } from './api/types';
import { Dashboard } from './dashboard/Dashboard';
import { TopicDetail } from './detail/TopicDetail';

export default function App() {
  const [tab, setTab] = useState('summary');
  const [data, setData] = useState<DashboardPayload>();
  const [error, setError] = useState('');
  const [attempt, setAttempt] = useState(0);
  const [selection, setSelection] = useState<{ id: string; candidate?: Candidate }>();
  const [announcement, setAnnouncement] = useState('');
  const watchlist = useLocalData<string[]>(WATCHLIST_KEY, [], isWatchlist);
  const reviews = useLocalData<Review[]>(REVIEWS_KEY, [], isReviews);
  const dialog = useRef<HTMLDialogElement>(null);
  const previousFocus = useRef<HTMLElement | null>(null);
  useEffect(() => {
    const controller = new AbortController();
    setError('');
    getDashboard(controller.signal).then(value => { if (!controller.signal.aborted) setData(value); }).catch(() => { if (!controller.signal.aborted) setError('요약 데이터를 불러오지 못했습니다. 연결 상태를 확인하고 다시 시도하세요.'); });
    return () => controller.abort();
  }, [attempt]);
  useEffect(() => {
    if (selection && dialog.current && !dialog.current.open) {
      previousFocus.current = document.activeElement as HTMLElement;
      if (dialog.current.showModal) dialog.current.showModal();
      else dialog.current.setAttribute('open', '');
    }
    if (selection && dialog.current) dialog.current.scrollTop = 0;
  }, [selection]);
  function close() {
    dialog.current?.close?.();
    setSelection(undefined);
    if (previousFocus.current?.isConnected) previousFocus.current.focus();
  }
  function toggleSave(id: string) {
    const exists = watchlist.value.includes(id);
    watchlist.save(exists ? watchlist.value.filter(item => item !== id) : [...watchlist.value, id]);
    setAnnouncement(exists ? '관심 목록에서 해제했습니다.' : '관심 목록에 저장했습니다.');
  }
  return <>
    <a className="skip" href="#main">본문으로 건너뛰기</a>
    <aside className="sidebar"><a className="brand" href={import.meta.env.BASE_URL} aria-label="Fieldnote 홈"><span className="brand-mark">↗</span>fieldnote<span className="brand-dot">.</span></a><p className="sidebar-caption">TECHNOLOGY OBSERVATORY</p>
      <nav aria-label="주요 메뉴">{[{ id: 'summary', icon: '◫', name: '오늘의 레이더' }, { id: 'graph', icon: '⌘', name: '기술 관계도' }, { id: 'saved', icon: '☆', name: '관심 목록' }].map(item => <button key={item.id} className={`nav-button ${tab === item.id ? 'active' : ''}`} aria-current={tab === item.id ? 'page' : undefined} onClick={() => setTab(item.id)}><span aria-hidden="true">{item.icon}</span>{item.name}{item.id === 'saved' && <span className="count">{watchlist.value.length}</span>}</button>)}</nav>
      <button className="export-button" onClick={() => exportLocalData(reviews.value, watchlist.value)}>리뷰 · 관심 JSON 내보내기</button>
      <div className="sidebar-bottom"><span className="status-dot" />PHYSICAL AI<p>논문에서 신호를 찾고,<br />관계 속에서 맥락을 읽습니다.</p><small>PERSONAL RESEARCH RADAR</small></div>
    </aside>
    <main id="main" tabIndex={-1}><header className="topbar"><span>개인 연구 관측소 <span className="muted">/ Physical AI</span></span><span>기준 {data ? formatTime(data.as_of) : '확인 중'}</span></header>
      {import.meta.env.VITE_DEMO_DATA !== 'false' && <div className="demo-banner"><strong>DEMO</strong><span>모든 수치·문헌·요약·기술 관계는 합성 예시입니다. 실제 연구 평가나 미래 성장 예측이 아닙니다.</span></div>}
      <section className="page-heading"><div><p className="eyebrow">FOLLOW THE SIGNAL, FIND THE CONTEXT</p><h1>{tab === 'graph' ? '기술은 서로 연결됩니다.' : tab === 'saved' ? '계속 지켜볼 질문들.' : '다음 움직임의 단서.'}</h1><p>{tab === 'saved' ? '다시 살펴보고 싶은 기술을 나만의 관측 목록에 모았습니다.' : 'Physical AI의 연구 흐름부터 새롭게 등장한 질문까지, 한눈에 살펴보세요.'}</p></div><div className="issue">FIELDNOTES<span>PHYSICAL AI / DAILY</span></div></section>
      <div role="status" aria-live="polite" className={watchlist.warning || reviews.warning ? 'uncertainty' : 'sr-only'}>{watchlist.warning || reviews.warning || announcement}</div>
      {tab === 'graph' ? <section className="empty"><p className="eyebrow">EXPLORE THE CONNECTIONS</p><h2>기술 관계도를 준비하고 있습니다.</h2><p>현재는 오늘의 레이더에서 기술별 근거를 살펴볼 수 있습니다.</p></section> : error ? <div className="empty" role="alert"><p>{error}</p><button onClick={() => setAttempt(attempt + 1)}>다시 불러오기</button></div> : data ? <Dashboard key={tab} data={data} saved={watchlist.value} savedOnly={tab === 'saved'} onSave={toggleSave} onSelect={(id, candidate) => setSelection({ id, candidate: candidate ?? [...data.candidates, ...data.growth_watchlist, ...data.community_candidates].find(c => c.entity_id === id) })} /> : <p role="status">레이더를 불러오는 중…</p>}
      <footer>FIELDNOTE <span>작은 신호를 모아, 더 나은 질문으로.</span><span>매일 07:00 Asia/Seoul</span></footer>
    </main>
    {selection && <dialog ref={dialog} aria-labelledby="detail-title" onCancel={e => { e.preventDefault(); close(); }} onClick={e => { if (e.target === dialog.current && e.clientX < dialog.current!.getBoundingClientRect().left) close(); }}><div className="drawer-top"><span className="eyebrow">TECHNOLOGY BRIEF</span><button className="icon-button" aria-label="상세 닫기" autoFocus onClick={close}>✕</button></div><TopicDetail key={selection.id} {...selection} asOf={data?.as_of} saved={watchlist.value.includes(selection.id)} onSave={toggleSave} review={reviews.value.find(r => r.candidate_id === selection.candidate?.id)} onReview={review => reviews.save([...reviews.value.filter(r => r.candidate_id !== review.candidate_id), review])} /></dialog>}
  </>;
}
