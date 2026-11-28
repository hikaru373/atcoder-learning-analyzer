import './Footer.css'

type FooterLink = {
  label: string
  href: string
  external?: boolean
}

const links: FooterLink[] = [
  { label: 'このサイトについて', href: '/about' },
  { label: '製作者', href: 'https://hikaru373.github.io/portfolio/', external: true },
  { label: 'GitHub', href: 'https://github.com/hikaru373/atcoder-learning-analyzer', external: true },
  { label: 'お問い合わせ', href: 'https://forms.gle/PiDUpJXJmxxBMm5K7', external: true },
]

function Footer() {
  return (
    <footer>
      <div className="footer-links">
        {links.map((link) => (
          <a key={link.label} href={link.href} target={link.external ? '_blank' : undefined}>
            {link.label}
          </a>
        ))}
      </div>
      <p>© 2026 AtCoder Learning Analyzer</p>
    </footer>
  )
}

export default Footer
