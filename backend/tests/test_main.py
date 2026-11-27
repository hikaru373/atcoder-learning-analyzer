import json
from datetime import datetime, timedelta, timezone

import pytest

from backend import main


# 難易度範囲
@pytest.mark.parametrize(
    "rating, expected",
    [
        (0, (0, 399, "#808080")),           # 灰
        (400, (400, 799, "#804000")),       # 茶
        (800, (800, 1199, "#008000")),      # 緑
        (1200, (1200, 1599, "#00C0C0")),    # 水
        (1600, (1600, 1999, "#0000FF")),    # 青
        (2000, (2000, 2399, "#C0C000")),    # 黄
        (2400, (2400, 2799, "#FF8000")),    # 橙
        (2800, (2800, 3199, "#FF0000")),    # 赤
        (3200, (3200, 3599, "#FF0000")),    # 赤
        (3600, (3600, 3999, "#FF0000")),    # 3600 以上は 3600〜3999
        (5000, (3600, 3999, "#FF0000")),    # 4000 を超えても 3600〜3999
    ],
)
def test_rating_classify(rating, expected):
    assert main.rating_classify(rating) == expected



# レーティング推定
def contest(perf, days_ago=0, rated=True):
    end = datetime.now(timezone.utc) - timedelta(days=days_ago)
    return {"IsRated": rated, "InnerPerformance": perf, "EndTime": end.isoformat()}

@pytest.mark.parametrize(
    "history, expected",
    [
        ([], 0),                                # 履歴なし
        ([contest(2000, rated=False)], 0),      # Unrated は無視
        ([contest(1600)], 1600),                # 1回だけならそのまま
        ([contest(-300)], 0),                   # 負は 0
        ([contest(1000, days_ago=730)], 950),   # 2年前は 5% 引き
        ([contest(1000, days_ago=3650)], 850),  # 古すぎても最大 15% 引き
    ],
)

    # 基本ケース・日付の重み
def test_estimate_rating(history, expected):
    assert main.estimate_rating(history) == expected

    # 履歴順の重み
def test_estimate_rating_recent_weighs_more():
    history = [contest(0)] * 4 + [contest(2000)] * 4  # 後ろほど新しい
    assert main.estimate_rating(history) > 1000



# ユーザーが存在しない場合
def test_analyze_unknown_user(client):
    res = client.post("/analyze", data={"user": "nobody"})
    assert "ユーザー名が存在しません" in res.text


# 分析が成功した場合
def test_analyze(client, fake_redis, histories):
    histories["alice"] = [contest(1300)]
    res = client.post("/analyze", data={"user": "alice"})
    assert ">1300</span>" in res.text   # 推定レート
    assert "1200 - 1599" in res.text    # 推奨Diff
    assert json.loads(fake_redis.get("user:alice"))["rating"] == 1300   # Redis に保存


# ランダム問題抽選
@pytest.mark.parametrize(
    "rating, expected",
    [
        (1300, "abc002_c"),   # 1300 // 400 = 3 番目の帯
        (9999, "agc001_f"),   # 4400 以上は 10 番目の帯に丸める
    ],
)
def test_random(client, rating, expected):
    res = client.get("/random", params = {"rating": rating})
    assert res.json()["random_problem"]["id"] == expected
