import { expect, test } from '../../frontend/node_modules/@playwright/test/index.js';
import fs from 'node:fs';
import path from 'node:path';

// Pin synthetic inputs independently of daily production exports.
test.beforeEach(async ({ page }) => {
  await page.route('**/data/**', async route => {
    const relative = decodeURIComponent(new URL(route.request().url()).pathname.split('/data/')[1]);
    const file = path.resolve(__dirname, 'data', relative);
    try {
      const body = fs.readFileSync(file);
      await route.fulfill({ contentType: 'application/json', body });
    } catch {
      await route.fulfill({ status: 404, body: '{}' });
    }
  });
});

test('summary → detail → graph evidence → review → reload persists', async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('./');
  await page.getByRole('button', { name: 'Tactile Learning 상세 보기' }).first().click();
  await expect(page.getByRole('link', { name: '촉각 학습 데모 문헌', exact: true })).toHaveAttribute('href', 'https://example.org/radar/tactile');
  await page.keyboard.press('Escape');
  await page.getByRole('button', { name: '기술 관계도', exact: true }).click();
  await expect(page.locator('canvas').first()).toBeVisible();
  await page.getByRole('button', { name: 'Tactile Learning 선택', exact: true }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByLabel('유용했나요?').selectOption('true');
  await page.getByLabel('검토 시간 (분)').fill('2.5');
  await page.getByRole('button', { name: '리뷰 저장', exact: true }).click();
  await page.getByRole('button', { name: '☆ 관심 저장', exact: true }).click();
  await page.keyboard.press('Escape');
  await page.getByRole('button', { name: 'World Models 선택', exact: true }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.getByRole('region', { name: '선택한 노드의 근거' })).toContainText('review:');
  await expect(page.getByRole('link', { name: '원문 근거' }).first()).toHaveAttribute('href', /^https:\/\//);
  await page.getByLabel('기술', { exact: true }).uncheck();
  await expect(page.getByText('현재 화면에서 숨겨진 노드입니다. 선택과 근거는 유지됩니다.')).toBeVisible();
  await page.reload();
  await page.getByRole('button', { name: /관심 목록/ }).click();
  await page.getByRole('button', { name: 'Tactile Learning 상세 보기' }).first().click();
  await expect(page.getByLabel('유용했나요?')).toHaveValue('true');
  await expect(page.getByLabel('검토 시간 (분)')).toHaveValue('2.5');
  expect(errors).toEqual([]);
});

test('mobile graph fits viewport', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('./');
  await page.getByRole('button', { name: '기술 관계도', exact: true }).click();
  await expect(page.getByRole('button', { name: '확대', exact: true })).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
});

test('graph loading failure can retry', async ({ page }) => {
  let attempts = 0;
  await page.route('**/data/graph.json', async route => {
    if (++attempts === 1) return route.fulfill({ status: 503, body: '{}' });
    return route.fulfill({ contentType: 'application/json',
      body: fs.readFileSync(path.resolve(__dirname, 'data/graph.json')) });
  });
  await page.goto('./');
  await page.getByRole('button', { name: '기술 관계도', exact: true }).click();
  await expect(page.getByRole('alert')).toContainText('관계 데이터를 불러오지 못했습니다.');
  await page.getByRole('button', { name: '다시 불러오기', exact: true }).click();
  await expect(page.getByRole('button', { name: 'World Models 선택', exact: true })).toBeVisible();
});
