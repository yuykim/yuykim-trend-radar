import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { TopicDetail } from './TopicDetail';
import App from '../App';
import data from '../../public/data/dashboard.json';
import tactile from '../../public/data/topics/tactile.json';
import world from '../../public/data/topics/world.json';
import jepa from '../../public/data/topics/jepa.json';
import vla from '../../public/data/topics/vla.json';

function mockData(topic: unknown = tactile) {
  vi.stubGlobal('fetch', vi.fn(async (url: string) => ({ ok: true, json: async () => url.endsWith('dashboard.json') ? data : url.includes('tactile') ? topic : url.includes('jepa') ? jepa : url.includes('vla') ? vla : world })));
}
describe('topic detail', () => {
  it('labels_preprint_and_unverified_summary', async () => {
    mockData(); render(<TopicDetail id="tactile" />);
    expect(await screen.findByText('preprint · 동료심사 전')).toBeInTheDocument();
    expect(screen.getByText('LLM 생성, 원문 확인 필요')).toBeInTheDocument();
    expect(screen.getByText('초록 기반 · 본문 확인 안 됨')).toBeInTheDocument();
    expect(screen.getByRole('link', { name: '촉각 학습 데모 문헌' })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: '요약 출처: 촉각 학습 데모 문헌' })).toBeInTheDocument();
  });
  it('works without LLM and never invents observation values', async () => {
    mockData(world); render(<TopicDetail id="world" />);
    expect(await screen.findByText(/LLM 요약이 없습니다/)).toBeInTheDocument();
    expect(screen.getByText(/수집 누락 \(missing\)/)).toBeInTheDocument();
    expect(screen.queryByText('0%')).not.toBeInTheDocument();
  });
  it('saves review with unknown values and restores it', async () => {
    mockData();
    const app = render(<App />);
    fireEvent.click((await screen.findAllByRole('button', { name: 'Tactile Learning 상세 보기' }))[0]);
    const useful = await screen.findByLabelText('유용했나요?');
    fireEvent.change(useful, { target: { value: 'true' } });
    fireEvent.change(screen.getByLabelText('검토 시간 (분)'), { target: { value: '3.5' } });
    fireEvent.click(screen.getByRole('button', { name: '리뷰 저장' }));
    const reviews = JSON.parse(localStorage.getItem('yuykim-trend-radar:reviews')!);
    expect(reviews[0]).toMatchObject({ candidate_id: 'candidate-tactile', useful: true, relevant: null, minutes_spent: 3.5 });
    app.unmount(); render(<App />);
    fireEvent.click((await screen.findAllByRole('button', { name: 'Tactile Learning 상세 보기' }))[0]);
    expect(await screen.findByLabelText('유용했나요?')).toHaveValue('true');
  });
  it('handles source failure and malformed browser storage', async () => {
    localStorage.setItem('yuykim-trend-radar:watchlist', '{broken');
    mockData(); render(<App />);
    expect(screen.getByText(/브라우저 저장 데이터를 읽을 수 없습니다/)).toBeInTheDocument();
  });
  it('handles a missing topic', async () => {
    vi.stubGlobal('fetch', vi.fn(async () => ({ ok: false, status: 404 })));
    render(<TopicDetail id="unknown" />);
    expect(await screen.findByRole('alert')).toHaveTextContent('상세 데이터를 불러오지 못했습니다');
  });
  it('does not present unknown observation values as measured', async () => {
    mockData({ ...tactile, observations: [{ ...tactile.observations[0], state: 'unknown', value: 99 }] });
    render(<TopicDetail id="tactile" />);
    expect(await screen.findByText(/미확인 \(unknown\)/)).toBeInTheDocument();
    expect(screen.queryByText(/research_share_28d: 99/)).not.toBeInTheDocument();
  });
  it('reports blocked localStorage while keeping current interest selection', async () => {
    mockData();
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => { throw new Error('blocked'); });
    render(<App />);
    fireEvent.click(await screen.findByRole('button', { name: 'World Models 관심 저장' }));
    expect(screen.getByText(/브라우저 저장이 제한되어 현재 화면에서만 유지됩니다/)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'World Models 관심 해제' })).toHaveAttribute('aria-pressed', 'true');
  });
});
