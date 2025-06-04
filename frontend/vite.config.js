import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  root: '.',         // 👈 ensure Vite looks in the current directory
  plugins: [react()],
  server: {
    port: 5173,
    open: true
  }
});
