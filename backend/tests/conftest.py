import os

# main.py は import 時に REDIS_URL を読むので、先にダミー値を入れておく
os.environ.setdefault("REDIS_URL", "redis://localhost:6379")

import fakeredis
import pytest
from fastapi.testclient import TestClient

from backend import main

# kenkoooo の problem-models.json の代わり
PROBLEM_MODELS = {
    "abc001_a": {"difficulty": 100},
    "abc002_c": {"difficulty": 1300},
    "agc001_f": {"difficulty": 5000},
    "abc003_x": {},  # difficulty なし
}

# AtCoder のコンテスト履歴の代わり（ユーザー名 → 履歴）
HISTORIES = {}


class FakeResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data


def fake_get(url):
    if "kenkoooo" in url:
        return FakeResponse(200, PROBLEM_MODELS)
    user = url.split("/")[-3]  # https://atcoder.jp/users/{user}/history/json
    if user in HISTORIES:
        return FakeResponse(200, HISTORIES[user])
    return FakeResponse(404, None)


@pytest.fixture
def fake_redis(monkeypatch):
    fake = fakeredis.FakeRedis()
    monkeypatch.setattr(main, "r", fake)
    monkeypatch.setattr(main.requests, "get", fake_get)
    HISTORIES.clear()
    return fake


@pytest.fixture
def histories(fake_redis):
    return HISTORIES


@pytest.fixture
def client(fake_redis):
    return TestClient(main.app)
