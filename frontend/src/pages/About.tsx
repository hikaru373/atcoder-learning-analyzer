import './About.css'

type FaqItem = {
  question: string
  answer: string
}

const faqItems: FaqItem[] = [
  {
    question: '推定レーティングとは何ですか？',
    answer:
      '現在の実力を把握するため、直近5回のRatedコンテストのPerformanceの平均値を「推定レーティング」としています。',
  },
  {
    question: '推奨問題はどのように選ばれますか？',
    answer:
      'AtCoder Problemsの問題データをもとに、推定レーティングと同じ色から問題を表示しています。',
  },
  {
    question: '推定レーティングが0になることがあります。',
    answer:
      'AtCoderではPerformanceが負になる場合があります。そのため、平均値が0以下となり、推定レーティングが0と表示されることがあります。',
  },
  {
    question: 'データはいつ更新されますか？',
    answer:
      'キャッシュを利用しているため、推定レーティング・問題データの更新には最大24時間かかる場合があります。',
  },
  {
    question: 'AtCoderの公式サービスですか？',
    answer: 'いいえ。本サイトは個人が開発・運営している非公式サービスです。',
  },
]

function About() {
  return (
    <>
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
          <h2>よくある質問（Q&amp;A）</h2>
          {faqItems.map((item) => (
            <details key={item.question}>
              <summary>{item.question}</summary>
              <p>{item.answer}</p>
            </details>
          ))}
        </section>
      </div>

      <footer>
        <div className="footer-links">
          <a href="#">このサイトについて</a>
          <a href="https://hikaru373.github.io/portfolio/" target="_blank">
            製作者
          </a>
          <a href="https://github.com/hikaru373/atcoder-learning-analyzer" target="_blank">
            GitHub
          </a>
          <a href="https://forms.gle/PiDUpJXJmxxBMm5K7" target="_blank">
            お問い合わせ
          </a>
        </div>
        <p>© 2026 AtCoder Learning Analyzer</p>
      </footer>
    </>
  )
}

export default About
