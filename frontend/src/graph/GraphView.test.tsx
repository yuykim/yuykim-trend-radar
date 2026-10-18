import { act, fireEvent, render, screen, within } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { GraphPayload } from '../api/types';
import { GraphView } from './GraphView';

const engine = vi.hoisted(() => ({ destroy: vi.fn(), resize: vi.fn(), batch: vi.fn((fn: () => void) => fn()),
  elements: vi.fn(() => ({ remove: vi.fn() })), add: vi.fn(),
  on: vi.fn((_event: string, _selector: unknown, _handler?: (event: { target: { data: () => string } }) => void) => {}), zoom: vi.fn(),
  pan: vi.fn(), getElementById: vi.fn(() => ({ select: vi.fn() })),
}));
vi.mock('cytoscape', () => ({ default: vi.fn(() => engine) }));
const data: GraphPayload = {
  generated_at: '2026-10-17T22:00:00Z',
  nodes: [{ id: 'tech', label: 'World Models', type: 'technology' },
    { id: 'company', label: 'Example Company', type: 'company' }],
  edges: [{ id: 'e', source_id: 'company', target_id: 'tech', relation: 'authored_research',
    evidence_url: 'https://example.org/source', evidence_location: 'section 3',
    available_at: null, review_status: 'proposed' }],
};
describe('GraphView', () => {
  beforeEach(() => { engine.on.mockClear(); });
  it('test_layer_switch_preserves_selected_node', () => {
    const onSelect = vi.fn();
    render(<GraphView data={data} onSelect={onSelect} />);
    fireEvent.click(screen.getByRole('button', { name: '확대' }));
    fireEvent.click(screen.getByRole('button', { name: 'Example Company 선택' }));
    expect(onSelect).toHaveBeenCalledWith('company');
    fireEvent.click(screen.getByRole('checkbox', { name: '기업' }));
    const panel = screen.getByRole('region', { name: '선택한 노드의 근거' });
    expect(within(panel).getByRole('heading', { name: 'Example Company' })).toBeInTheDocument();
    expect(within(panel).getByRole('link', { name: '원문 근거' })).toHaveAttribute('href', 'https://example.org/source');
    expect(within(panel).getByText('section 3')).toBeInTheDocument();
    expect(within(panel).getByText('시점 unknown')).toBeInTheDocument();
    expect(within(panel).getByText('review: proposed')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: '축소' }));
    fireEvent.change(screen.getByLabelText('관계 필터'), { target: { value: 'correlation' } });
    expect(within(panel).getByRole('link', { name: '원문 근거' })).toBeInTheDocument();
    expect(onSelect).toHaveBeenCalledTimes(1);
  });
  it('keeps selection and evidence when props refresh', () => {
    const onSelect = vi.fn();
    const view = render(<GraphView data={data} onSelect={onSelect} />);
    fireEvent.click(screen.getByRole('button', { name: 'World Models 선택' }));
    view.rerender(<GraphView data={{ ...data, nodes: [], edges: [] }} onSelect={onSelect} />);
    expect(screen.getByRole('link', { name: '원문 근거' })).toBeInTheDocument();
    expect(screen.getByText('표시할 노드가 없습니다. 레이어를 조정하세요.')).toBeInTheDocument();
  });
  it('handles canvas selection, zoom, cleanup and an empty graph', () => {
    const onSelect = vi.fn();
    const view = render(<GraphView data={data} onSelect={onSelect} />);
    const tap = engine.on.mock.calls.find(call => call[0] === 'tap');
    act(() => { tap?.[2]?.({ target: { data: () => 'tech' } }); });
    expect(onSelect).toHaveBeenCalledWith('tech');
    view.unmount();
    expect(engine.destroy).toHaveBeenCalled();
    render(<GraphView data={{ ...data, nodes: [], edges: [] }} onSelect={onSelect} />);
    expect(screen.getByText('표시할 노드가 없습니다. 레이어를 조정하세요.')).toBeInTheDocument();
  });
  it('never renders a script URL as an evidence link', () => {
    render(<GraphView data={{ ...data, edges: [{ ...data.edges[0], evidence_url: 'javascript:alert(1)' }] }} onSelect={vi.fn()} />);
    fireEvent.click(screen.getByRole('button', { name: 'World Models 선택' }));
    expect(screen.queryByRole('link', { name: '원문 근거' })).not.toBeInTheDocument();
    expect(screen.getByText('출처 URL unknown')).toBeInTheDocument();
  });
});
