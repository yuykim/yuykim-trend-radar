import { fireEvent, render, screen, within } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import App from '../App';
import { Dashboard } from './Dashboard';
import data from '../../../tests/e2e/data/dashboard.json';
import world from '../../../tests/e2e/data/topics/world.json';
import tactile from '../../../tests/e2e/data/topics/tactile.json';
import jepa from '../../../tests/e2e/data/topics/jepa.json';
import vla from '../../../tests/e2e/data/topics/vla.json';
import type { DashboardPayload } from '../api/types';

export function mockData() {
  vi.stubGlobal('fetch', vi.fn(async (url: string) => ({ ok: true, json: async () => url.endsWith('dashboard.json') ? data : url.includes('tactile') ? tactile : url.includes('jepa') ? jepa : url.includes('vla') ? vla : world })));
}
describe('dashboard', () => {
  it('shows_missing_and_low_support', async () => {
    mockData();
    render(<Dashboard data={data as DashboardPayload} saved={[]} onSave={() => {}} onSelect={() => {}} />);
    const missing = await screen.findByRole('article', { name: 'JEPA' });
    expect(within(missing).getByText(/수집 누락/)).toBeInTheDocument();
    expect(missing).not.toHaveTextContent('0%');
    expect(missing).not.toHaveTextContent('0건');
    expect(screen.getByText('표본 부족 · low_support · 변화 해석 주의')).toBeInTheDocument();
    expect(screen.getByText(/openreview: 수집 실패/)).toBeInTheDocument();
  });
  it('opens_topic_evidence', async () => {
    mockData();
    render(<App />);
    fireEvent.click(await screen.findByRole('button', { name: 'World Models 상세 보기' }));
    expect(await screen.findByRole('link', { name: 'World Model 데모 문헌' })).toHaveAttribute('href', 'https://example.org/radar/world');
    expect(screen.getAllByText(/2026-10-18 07:00 KST/).length).toBeGreaterThan(0);
    expect(screen.getByText(/최초 공개/)).toBeInTheDocument();
  });
  it('keeps watchlist after remount and filters cards', async () => {
    mockData();
    const app = render(<App />);
    fireEvent.click(await screen.findByRole('button', { name: 'World Models 관심 저장' }));
    expect(JSON.parse(localStorage.getItem('yuykim-trend-radar:watchlist')!)).toEqual(['world']);
    app.unmount(); render(<App />);
    fireEvent.click(screen.getByRole('button', { name: /관심 목록/ }));
    expect(await screen.findByRole('button', { name: 'World Models 상세 보기' })).toBeInTheDocument();
    fireEvent.change(screen.getByRole('searchbox'), { target: { value: 'no-match' } });
    expect(screen.getByText('일치하는 기술이 없습니다.')).toBeInTheDocument();
  });
  it('shows dashboard failure with retry', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new Error('offline')));
    render(<App />);
    expect(await screen.findByRole('button', { name: '다시 불러오기' })).toBeInTheDocument();
  });
  it('shows all four empty sections', () => {
    render(<Dashboard data={{ ...data, trends: [], candidates: [], growth_watchlist: [], community_candidates: [] } as DashboardPayload} saved={[]} onSave={() => {}} onSelect={() => {}} />);
    expect(screen.getAllByText('아직 표시할 자료가 없습니다.')).toHaveLength(4);
  });
});
