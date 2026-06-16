# 目次
1. 概要
2. 主な機能
3. 使い方
4. セットアップ手順
5. ディレクトリ構成
6. 使用技術
<br><br>
# ① 概要
AtCoderのユーザー名を入力すると、過去のコンテスト結果から推定レーティングを算出し、学習に適した問題難易度帯を表示します。
推薦された難易度帯の問題一覧ページへ直接アクセスできるため、効率的な競技プログラミング学習を支援します。

<br><br>
# ② 主な機能
+ AtCoderユーザー情報の取得
+ コンテスト履歴の分析
+ 推定レーティングの算出
+ 学習推奨Diff帯の表示
+ 問題一覧ページへのリンク生成
+ Redisによるキャッシュ機能

<br><br><br><br>
# ③ 使い方
[こちらのサイトから](https://atcoder-learning-analyzer.onrender.com)

<br><br>
# ④ セットアップ手順

<br><br>
# ⑤ ディレクトリ構成
├── main.py
├── requirements.txt
├── README.md
├── html
│    ├── input.html
│    └── result.html
└── static
    └── images
<br><br>
# ⑥ 使用技術
+ Python
+ FastAPI
+ HTML/CSS
+ Jinja2
+ Render
+ Redis
