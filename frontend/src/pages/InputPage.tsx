import { useState } from 'react'
import type { FormEvent } from 'react'
import Footer from '../components/Footer'
import '../styles/input.css'

export default function InputPage() {
  // 入力欄の値を React の state で管理する
  const [user, setUser] = useState('')

  function handleSubmit(e: FormEvent) {
    // フォーム送信によるページ遷移（リロード）を止める
    e.preventDefault()
    // TODO: ステップ3で結果画面（/result/ユーザー名）へ移動する
    console.log('分析するユーザー:', user.trim())
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
