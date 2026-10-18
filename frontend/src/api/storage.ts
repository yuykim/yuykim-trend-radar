import { useState } from 'react';
import type { Review } from './types';

export const REVIEWS_KEY = 'yuykim-trend-radar:reviews';
export const WATCHLIST_KEY = 'yuykim-trend-radar:watchlist';

function isReview(value: unknown): value is Review {
  if (value === null || typeof value !== 'object') return false;
  const r = value as Review;
  return typeof r.candidate_id === 'string' && typeof r.reviewed_at === 'string'
    && ['already_known', 'relevant', 'distinct', 'useful'].every(key => r[key as keyof Review] === null || typeof r[key as keyof Review] === 'boolean')
    && (r.minutes_spent === null || (Number.isFinite(r.minutes_spent) && r.minutes_spent >= 0));
}

export function useLocalData<T>(key: string, fallback: T, validate: (value: unknown) => value is T) {
  const [initial] = useState(() => {
    try {
      const raw = localStorage.getItem(key);
      if (raw === null) return { value: fallback, warning: '' };
      const parsed: unknown = JSON.parse(raw);
      if (!validate(parsed)) throw new Error('Invalid stored data');
      return { value: parsed, warning: '' };
    } catch { return { value: fallback, warning: '브라우저 저장 데이터를 읽을 수 없습니다. 현재 화면의 변경은 JSON으로 내보내 보관하세요.' }; }
  });
  const [value, setValue] = useState(initial.value);
  const [warning, setWarning] = useState(initial.warning);
  function save(next: T) {
    setValue(next);
    try { localStorage.setItem(key, JSON.stringify(next)); setWarning(''); }
    catch { setWarning('브라우저 저장이 제한되어 현재 화면에서만 유지됩니다. JSON으로 내보내 보관하세요.'); }
  }
  return { value, save, warning };
}
export const isWatchlist = (value: unknown): value is string[] => Array.isArray(value) && value.every(id => typeof id === 'string');
export const isReviews = (value: unknown): value is Review[] => Array.isArray(value) && value.every(isReview);

export function exportLocalData(reviews: Review[], watchlist: string[]) {
  const blob = new Blob([JSON.stringify({ exported_at: new Date().toISOString(), reviews, watchlist }, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'yuykim-trend-radar-personal.json';
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 0);
}
