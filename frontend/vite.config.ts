import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: '/yuykim-trend-radar/',
  // Never load the repository's batch environment file.
  envDir: false,
  plugins: [react()],
  test: {
    include: ['src/**/*.test.{ts,tsx}'],
    environment: 'jsdom',
    setupFiles: ['./src/testSetup.ts'],
    restoreMocks: true,
    clearMocks: true,
  },
});
