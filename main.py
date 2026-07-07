from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import redis
import json
import random

app = FastAPI()
templates = Jinja2Templates(directory="html")

# HTML
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")


# Redis
import os
r = redis.from_url(os.getenv("REDIS_URL"))


problems = []
#問題難易度
def problem():
    global problems
    models = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json").json()
    if len(problems) == len(models):
        return problems
    else:
        tmp_id = {x["id"] for x in problems}
        for id, data in models.items():
            if id not in tmp_id:
                problems.append({ "id": id, "difficulty": data.get["difficulty"] })
        return problems
#ランダム
def random_problem():
    return random.choice(problem())


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
    color=["#808080","#804000","#008000","#00C0C0","#0000FF","#C0C000","#FF8000","#FF0000"]
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
    cached = r.get(user)
    if cached:
        result = json.loads(cached.decode("utf-8"))
        result["cached"] = True
        result["random_problem"] = random_problem()
        return templates.TemplateResponse(request ,"result.html" ,result )

    history = fetch_history(user)
    # ユーザー名が存在しない
    if not history:
        return templates.TemplateResponse(request, "result.html", {"user": user, "error": "ユーザー名が存在しません"})

    # レーティング分析
    rating = estimate_rating(history)
    from_diff,to_diff,color = rating_classify(rating)

    url = f"https://kenkoooo.com/atcoder/#/list?fromDiff={from_diff}&toDiff={to_diff}"
    result = {"user": user, "rating": rating, "from_diff": from_diff, "to_diff": to_diff, "url": url ,"color": color}
    
    # Redisに保存（期限：1日）
    r.set(user, json.dumps(result), ex=86400)

    result["cached"] = False
    
    #ランダム
    result["random_problem"] = random_problem()
    return templates.TemplateResponse(request ,"result.html" ,result )




