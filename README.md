# 目次
1. 概要
2. 主な機能
3. 背景
4. 使い方
5. セットアップ手順
6. ディレクトリ構成
7. データ構造
8. 使用技術
9. 終わりに
<br><br><br>
# ① 概要
![結果画面](https://github.com/user-attachments/assets/7eb4ee36-887d-4d18-b246-db4dae84e190)
<br>
AtCoderのユーザー名を入力すると、過去のコンテスト結果から推定レーティングを算出し、現在の実力に適した問題をランダムに表示します。また、推定された難易度帯の問題一覧ページへ直接アクセスできるため、効率的な競技プログラミング学習を支援します。<br>
本サイトの利用により発生した損害や不利益について、開発者は一切の責任を負いません。あらかじめご了承ください。
<br><br><br>
# ② 背景
競技プログラミング学習では、実力に合った問題を選ぶのに手間がかかることや、レートだけでは現在の実力を正確に把握しづらいという課題がありました。そこで、提出履歴とパフォーマンスを分析して実力を推定し、最適な難易度の問題を推薦することで、効率的な学習を支援するシステムを開発しました。
<br><br><br>
# ③ 主な機能
+ AtCoderユーザー情報の取得
+ コンテスト履歴の分析
+ 推定レーティングの算出
+ 学習推奨Diff帯の表示
+ 問題一覧ページへのリンク生成
+ Redisによるキャッシュ機能
<br><br><br>
# ④ 使い方
[こちらのサイトから](https://atcoder-learning-analyzer.onrender.com)<br>
<video src="https://github.com/user-attachments/assets/55353321-fbb7-4cf4-aec2-03c45b0e98cc" controls width="100%">
</video>
<br><br><br>
# ⑤ セットアップ手順
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
# ⑥ ディレクトリ構成
<pre>
test
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
# ⑦ データ構造
Redisのキャッシュ構造です。（TTL：24時間）
![データ構造](https://github.com/user-attachments/assets/74a7fc6a-7c83-4d6b-9efa-7676f9756a3d)
<br><br><br>
# ⑧ 使用技術
+ **フロントエンド**：HTML、CSS
+ **バックエンド**：Python、FastAPI、Jinja2
+ **データベース**：Redis
+ **インフラ**：Render
+ **バージョン管理**：Git、GitHub
+ **動作確認環境環境**：macOS 15.6

### 選定理由
+ **FastAPI**：APIの実装がシンプルで、処理性能が高く、高速なWebアプリケーションを開発できるため。
+ **Redis**：キャッシュを利用して処理を高速化し、外部APIへのアクセス回数を削減するため。また、データは毎日更新される一方で、データ量はそこまで多くないため、有効期限の管理がしやすいRedisを採用した。

<br><br><br>
# ⑨ 終わりに
最後までご覧いただき、ありがとうございました。<br>
このアプリが競技プログラミングの上達に少しでも役立てば嬉しいです。<br>
バグ報告や機能要望などがございましたら、以下よりお気軽にご連絡ください。
<br>
- [お問い合わせフォーム](https://forms.gle/PiDUpJXJmxxBMm5K7)
- [GitHub Issues](https://github.com/hikaru373/atcoder-learning-analyzer/issues)
- [メール](mailto:star3.14wars.sh@gmail.com)