from backend import main


def test_rating_classify():
    assert main.rating_classify(1200) == (1200, 1599, "#00C0C0")
