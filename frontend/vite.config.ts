import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
<<<<<<< HEAD
  plugins: [svelte()],
  server: {
    proxy: {
        '/api': 'http://localhost:5000'
    }
    }
})
=======
	plugins: [sveltekit()]
});
>>>>>>> Frontend-Svelte
