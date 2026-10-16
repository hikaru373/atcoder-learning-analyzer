import Footer from '../components/Footer'
import '../styles/about.css'

// Q&A はデータとして持ち、map で描画する（追加するときはここに1件足すだけ）
const faqs = [
  {
    question: '推定レーティングとは何ですか？',
    answer: '現在の実力を把握するため、直近5回のRatedコンテストのPerformanceの平均値を「推定レーティング」としています。',
  },
  {
    question: '推奨問題はどのように選ばれますか？',
    answer: 'AtCoder Problemsの問題データをもとに、推定レーティングと同じ色から問題を表示しています。',
  },
  {
    question: '推定レーティングが0になることがあります。',
    answer: 'AtCoderではPerformanceが負になる場合があります。そのため、平均値が0以下となり、推定レーティングが0と表示されることがあります。',
  },
  {
    question: 'データはいつ更新されますか？',
    answer: 'キャッシュを利用しているため、推定レーティング・問題データの更新には最大24時間かかる場合があります。',
  },
  {
    question: 'AtCoderの公式サービスですか？',
    answer: 'いいえ。本サイトは個人が開発・運営している非公式サービスです。',
  },
]

export default function AboutPage() {
  return (
    <div className="about-page">
      <title>このサイトについて</title>

      <div className="container">
        <h1>このサイトについて</h1>

        <section>
          <h2>概要</h2>
          <p>
            このWebアプリは、AtCoderのユーザー名を入力すると、過去のコンテスト結果から現在の実力を推定し、そのレベルに適した問題を表示する競技プログラミング学習支援ツールです。
          </p>
        </section>

        <section>
          <h2>よくある質問（Q&A）</h2>
          {faqs.map((faq) => (
            <details key={faq.question}>
              <summary>{faq.question}</summary>
              <p>{faq.answer}</p>
            </details>
          ))}
        </section>
      </div>

      <Footer />
    </div>
  )
}
