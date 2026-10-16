import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router'
import './styles/global.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {/* BrowserRouter で囲むと、中のコンポーネントで URL を扱えるようになる */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
