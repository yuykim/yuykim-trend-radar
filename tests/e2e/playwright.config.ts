import { defineConfig } from '../../frontend/node_modules/@playwright/test/index.js';

export default defineConfig({
  testDir: '.',
  outputDir: '../../frontend/test-results/task7',
  reporter: 'list',
  use: { baseURL: 'http://127.0.0.1:4173/yuykim-trend-radar/',
    channel: process.env.CI ? 'chromium' : 'msedge', headless: true },
  webServer: {
    command: 'npm --prefix frontend run preview -- --host 127.0.0.1 --port 4173 --strictPort',
    cwd: '../..',
    url: 'http://127.0.0.1:4173/yuykim-trend-radar/',
    reuseExistingServer: false,
  },
});
