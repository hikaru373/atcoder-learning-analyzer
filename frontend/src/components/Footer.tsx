import { Link } from 'react-router'

// 全ページ共通のフッター
export default function Footer() {
  return (
    <footer>
      <div className="footer-links">
        {/* サイト内の移動は Link（ページを読み込み直さない）、外部サイトは a */}
        <Link to="/about">このサイトについて</Link>
        <a href="https://hikaru373.github.io/portfolio/" target="_blank">製作者</a>
        <a href="https://github.com/hikaru373/atcoder-learning-analyzer" target="_blank">GitHub</a>
        <a href="https://forms.gle/PiDUpJXJmxxBMm5K7" target="_blank">お問い合わせ</a>
      </div>
      <p>© 2026 AtCoder Learning Analyzer</p>
    </footer>
  )
}
