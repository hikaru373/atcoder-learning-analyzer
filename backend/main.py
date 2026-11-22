from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import requests
import redis
import json
import random
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "frontend" / "html")

# HTML
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# React（npm run build で生成される frontend/dist を配信）
DIST_DIR = BASE_DIR / "frontend" / "dist"
app.mount("/assets", StaticFiles(directory=DIST_DIR / "assets", check_dir=False), name="assets")


# Redis
import os
r = redis.from_url(os.getenv("REDIS_URL"))


#問題難易度
def problem():
    data = r.get("problems_classify")
    if data:
        problems_classify = json.loads(data.decode("utf-8"))
        return problems_classify
    else:
        problems_classify = [[] for _ in range(11)]
        models = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json").json()
        for id, data in models.items():
            if data.get("difficulty") is not None:
                problems_classify[min(max(data.get("difficulty")//400 ,0), 10)].append({ "id": id, "difficulty": data.get("difficulty") })
        r.set("problems_classify", json.dumps(problems_classify), ex = 24 * 60 * 60)
        return problems_classify
#ランダム
def random_problem(n):
    return random.choice(problem()[n])


# ユーザーのコンテスト履歴を取得
def fetch_history(user):
    url = f"https://atcoder.jp/users/{user}/history/json"
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

# レーティング推定
RECENT_CONTESTS = 6   # 直近何回のRatedコンテストを使うか
STRONG_CONTESTS = 3    # 直近何回を強く見るか（この回数の次の回で重みが半分になる）
DECAY_POWER = 4        # 強く見る回数を超えたあとの落ち方の急さ（大きいほど急）
SLOW_YEARS = 2         # この年数までは弱めに割り引く
SLOW_RATE = 0.05       # SLOW_YEARS 年の時点での割引率
FAST_RATE = 0.10       # SLOW_YEARS 年以降、1年あたりに増やす割引率
MAX_RATE = 0.15        # 割引率の上限（3年で達する）

# 最後に参加してからの年数に応じた割引率
def discount_rate(years):
    if years <= SLOW_YEARS:
        # (t / SLOW_YEARS)^2 の形で、最初はほとんど引かず、SLOW_YEARS 年に近づくほど増やす
        # SLOW_YEARS 年でちょうど SLOW_RATE になる
        return SLOW_RATE * (years / SLOW_YEARS) ** 2
    # SLOW_YEARS 年以降は1年あたり FAST_RATE ずつ増やし、MAX_RATE で止める
    return min(MAX_RATE, SLOW_RATE + FAST_RATE * (years - SLOW_YEARS))

def estimate_rating(history):
    if not history:
        return 0
    rated = [h for h in history if h.get("IsRated")]
    if not rated:
        return 0
    recent = rated[-RECENT_CONTESTS:]   # RECENT_CONTESTS 回に満たない場合はある分だけ

    now = datetime.now(timezone.utc)
    total = 0
    weight_sum = 0
    for i, h in enumerate(reversed(recent)):
        # 新しい方からi回目の重みを 1 / (1 + i/DECAY_SCALE)^2 にする
        weight = 1 / (1 + i / DECAY_SCALE) ** 2
        # 上限（ABCは2400など）で切られる前の値を使う
        perf = h["InnerPerformance"]
        # そのコンテストからの年数で割り引く
        # 絶対値 × 割引率 を引くので、負のパフォーマンスでも下がる方向に効く
        days = (now - datetime.fromisoformat(h["EndTime"])).days
        perf -= abs(perf) * discount_rate(days / 365)
        total += perf * weight
        weight_sum += weight
    return max(0, int(total / weight_sum))

# レーティング分類
def rating_classify(rating):
    color=["#808080", "#804000", "#008000", "#00C0C0", "#0000FF", "#C0C000", "#FF8000", "#FF0000", "#FF0000"]
    if rating>=3600:
        return 3600,3999,color[-1]
    else:
        base = rating // 400
        return base*400, (base + 1)*400-1 ,color[base]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request ,"input.html" )

@app.post("/analyze")
def analyze(request: Request, user = Form(...)):
    # Redisに存在するか
    cached = r.get(f"user:{user}")
    if cached:
        result = json.loads(cached.decode("utf-8"))
        result["random_problem"] = random_problem(min(result["rating"]//400,10))
        return templates.TemplateResponse(request ,"result.html" ,result )

    history = fetch_history(user)
    # ユーザー名が存在しない
    if not history:
        return templates.TemplateResponse(request, "result.html", {"user": user, "error": "ユーザー名が存在しません"})

    # レーティング分析
    rating = estimate_rating(history)
    from_diff,to_diff,color = rating_classify(rating)

    result = {"user": user, "rating": rating, "from_diff": from_diff, "to_diff": to_diff, "color": color}
    
    # Redisに保存（期限：1日）
    r.set(f"user:{user}", json.dumps(result), ex=60) ###
    
    #ランダム
    result["random_problem"] = random_problem(min(result["rating"]//400,10))
    return templates.TemplateResponse(request ,"result.html" ,result )

#ランダム更新
@app.get("/random")
def random_reload(rating: int):
    newProblem = random_problem(min(rating // 400, 10))
    return {"random_problem": newProblem}


#footer_このサイトについて
@app.get("/about")
def about():
    return FileResponse(DIST_DIR / "index.html")

@app.get("/favicon.ico")
def favicon():
    return FileResponse(DIST_DIR / "favicon.ico")