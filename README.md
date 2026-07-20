# 目次
1. 概要
2. 主な機能
3. 使い方
4. セットアップ手順
5. ディレクトリ構成
6. 使用技術
<br><br><br>
# ① 概要
AtCoderのユーザー名を入力すると、過去のコンテスト結果から推定レーティングを算出し、現在の実力に適した問題をランダムに表示します。また、推定された難易度帯の問題一覧ページへ直接アクセスできるため、効率的な競技プログラミング学習を支援します。<br>
本サイトの利用により発生した損害や不利益について、開発者は一切の責任を負いません。あらかじめご了承ください。
<br><br><br>
# ② 主な機能
+ AtCoderユーザー情報の取得
+ コンテスト履歴の分析
+ 推定レーティングの算出
+ 学習推奨Diff帯の表示
+ 問題一覧ページへのリンク生成
+ Redisによるキャッシュ機能
<br><br><br>
# ③ 使い方
[こちらのサイトから](https://atcoder-learning-analyzer.onrender.com)<br>
AtCoderのユーザー名を入力し、スタートボタンを押す。
<br><br><br>
# ④ セットアップ手順
### 1. リポジトリのクローン<br>
```
git clone https://github.com/hikaru373/atcoder-learning-analyzer.git
```
```
cd atcoder-learning-analyzer
```
### 2. 必要ライブラリのインストール<br>
```
pip install -r requirements.txt
```
### 3.環境変数の設定<br>
```
export REDIS_URL=redis://localhost:6379
```
### 4.サーバー起動<br>
```
uvicorn main:app --reload
```
<br><br>
# ⑤ ディレクトリ構成
<pre>
atcoder-learning-analyzer
├── main.py
├── requirements.txt
├── README.md
├── html
│    ├── input.html
│    └── result.html
└── static
    └── images
</pre>
<br><br><br>
# ⑥ 使用技術
+ Python
+ FastAPI
+ HTML/CSS
+ Jinja2
+ Render
+ Redis
<br><br><br>
# ⑦ 終わりに
最後までご覧いただき、ありがとうございました。<br>
このアプリが競技プログラミングの上達に少しでも役立てば嬉しいです。<br>
バグ報告や機能要望などがございましたら、以下よりお気軽にご連絡ください。
<br>
- [お問い合わせフォーム](https://forms.gle/PiDUpJXJmxxBMm5K7)
- [GitHub Issues](https://github.com/hikaru373/atcoder-learning-analyzer/issues)
- [メール](mailto:star3.14wars.sh@gmail.com)