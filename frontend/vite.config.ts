import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';

const sveltePlugins = await sveltekit();

export default defineConfig({
  resolve: process.env.VITEST
    ? { conditions: ['browser'] }
    : undefined,

  plugins: sveltePlugins as any,

  optimizeDeps: {
    include: ['svelte']
  },

  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/setupTests.js',
    include: ['tests/**/*.test.js']
  }
});
