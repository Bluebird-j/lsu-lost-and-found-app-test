import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // allow requests from your ngrok host
    allowedHosts: ['cuspidal-crackly-candy.ngrok-free.dev'],
  },
})
