import { useParams } from 'react-router'
import Footer from '../components/Footer'

// TODO: ステップ5で API から分析結果を取得して表示する（今は仮の画面）
export default function ResultPage() {
  // URL の /result/:user の部分を取り出す
  const { user } = useParams()

  return (
    <div>
      <title>Result</title>
      <h1>{user}</h1>
      <Footer />
    </div>
  )
}
