import { useState } from 'react'
import type { FormEvent } from 'react'
import { useNavigate } from 'react-router'
import Footer from '../components/Footer'
import '../styles/input.css'

export default function InputPage() {
  // 入力欄の値を React の state で管理する
  const [user, setUser] = useState('')
  const navigate = useNavigate()

  function handleSubmit(e: FormEvent) {
    // フォーム送信によるページ遷移（リロード）を止める
    e.preventDefault()
    const name = user.trim()
    if (!name) return
    // 結果画面へ移動（記号などが URL を壊さないようにエンコードする）
    navigate(`/result/${encodeURIComponent(name)}`)
  }

  return (
    <div className="input-page">
      <title>AtCoder Learning Analyzer</title>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="AtCoderのユーザー名"
          value={user}
          onChange={(e) => setUser(e.target.value)}
          required
        />
        <button type="submit">スタート</button>
      </form>

      <Footer />
    </div>
  )
}
