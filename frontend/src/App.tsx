import { Navigate, Route, Routes } from 'react-router'
import InputPage from './pages/InputPage'
import ResultPage from './pages/ResultPage'
import AboutPage from './pages/AboutPage'

// URL と表示する画面の対応表
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<InputPage />} />
      <Route path="/result/:user" element={<ResultPage />} />
      <Route path="/about" element={<AboutPage />} />
      {/* どれにも当てはまらない URL はトップへ戻す */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
