import { useEffect, useState } from 'react';
import type { DashboardPayload, GraphPayload, TopicDetail } from './types';

async function read<T>(path: string, signal?: AbortSignal): Promise<T> {
  const response = await fetch(`${import.meta.env.BASE_URL}data/${path}`, { signal });
  if (!response.ok) throw new Error(`데이터를 불러오지 못했습니다 (${response.status}).`);
  return response.json() as Promise<T>;
}
export const getDashboard = (signal?: AbortSignal) => read<DashboardPayload>('dashboard.json', signal);
export const getTopic = (id: string, signal?: AbortSignal) => read<TopicDetail>(`topics/${encodeURIComponent(id)}.json`, signal);
export const getGraph = (signal?: AbortSignal) => read<GraphPayload>('graph.json', signal);

export function useTopic(id: string) {
  const [state, setState] = useState<{ data?: TopicDetail; error?: string }>({});
  useEffect(() => {
    const controller = new AbortController();
    setState({});
    getTopic(id, controller.signal).then(data => {
      if (!controller.signal.aborted) setState({ data });
    }).catch(() => {
      if (!controller.signal.aborted) setState({ error: '상세 데이터를 불러오지 못했습니다. 잠시 후 다시 열어주세요.' });
    });
    return () => controller.abort();
  }, [id]);
  return state;
}

export function formatTime(value: string | null): string {
  if (value === null) return '미확인';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return '미확인';
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Seoul', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(date).map(p => [p.type, p.value]));
  return `${parts.year}-${parts.month}-${parts.day} ${parts.hour}:${parts.minute} KST`;
}

export function safeUrl(value: string): string | undefined {
  try {
    const url = new URL(value);
    return ['https:', 'http:'].includes(url.protocol) ? url.href : undefined;
  } catch { return undefined; }
}
