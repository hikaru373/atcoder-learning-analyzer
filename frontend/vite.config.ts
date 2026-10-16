import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // 開発中は /api へのリクエストを FastAPI（uvicorn）へ転送する
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
