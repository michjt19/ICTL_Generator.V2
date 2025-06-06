import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  root: '.',         // 👈 ensure Vite looks in the current directory
  plugins: [react()],
  server: {
    host: 0.0.0.0,
    port: 5173,
    host: true,
    open: false       // ✅ prevents xdg-open error
  }
});
