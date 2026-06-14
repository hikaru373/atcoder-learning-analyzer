from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import redis
import json

app = FastAPI()
templates = Jinja2Templates(directory="html")

# HTML
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Redis
### host
import os
r = redis.from_url(os.getenv("REDIS_URL"))


# ユーザーのコンテスト履歴を取得
def fetch_history(user):
    url = f"https://atcoder.jp/users/{user}/history/json"
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

# レーティング推定
def estimate_rating(history):
    if not history:
        return 0
    perf = [h.get("Performance") for h in history if h.get("IsRated")]
    if not perf:
        return 0
    return sum(perf[-5:]) // min(len(perf), 5)

# レーティング分類
def rating_classify(rating):
    if rating>=3600:
        return 3600,3999
    else:
        base = rating // 400
        return base*400, (base + 1)*400-1


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request ,"input.html" )

@app.post("/analyze")
def analyze(request: Request, user = Form(...)):
    # Redisに存在するか
    cached = r.get(user)
    if cached:
        result = json.loads(cached.decode("utf-8"))
        result["cached"] = True
        return templates.TemplateResponse(request ,"result.html" ,result )

    history = fetch_history(user)
    # ユーザー名が存在しない
    if not history:
        return templates.TemplateResponse(request, "result.html", {"user": user, "error": "ユーザー名が存在しません"})

    # レーティング分析
    rating = estimate_rating(history)
    from_diff,to_diff = rating_classify(rating)

    url = f"https://kenkoooo.com/atcoder/#/list?fromDiff={from_diff}&toDiff={to_diff}"
    result = {"user": user, "rating": rating, "from_diff": from_diff, "to_diff": to_diff, "url": url }

    # Redisに保存（期限：1日）
    r.set(user, json.dumps(result), ex=86400)

    result["cached"] = False
    return templates.TemplateResponse(request ,"result.html" ,result )




