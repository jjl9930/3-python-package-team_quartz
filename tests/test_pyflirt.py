from pyflirt import line, lines, categories
import pytest
from pyflirt import compliment
import re

def test_categories_present():
    assert "nerdy" in categories()

def test_line_seed_stable():
    assert line(category="nerdy", seed=42) == line(category="nerdy", seed=42)

def test_lines_len_and_content():
    arr = lines(n=3, name="Sam", seed=123)
    assert len(arr) == 3
    assert all(isinstance(s, str) and s for s in arr)

def test_cheese_bounds():
    import pytest
    with pytest.raises(ValueError):
        line(cheese=0)
    with pytest.raises(ValueError):
        lines(n=2, cheese=6)

def test_compliment_returns_string():
    """Should always return a non-empty string."""
    out = compliment()
    assert isinstance(out, str)
    assert len(out) > 0


def test_compliment_includes_name():
    """Name should appear in the compliment when provided."""
    result = compliment(role="developer", mood="nerdy", name="Alex", seed=1)
    assert "Alex" in result


def test_compliment_emojis_count():
    """Correct number of emojis should be appended."""
    result = compliment(role="data", emojis=3, seed=2)
    assert result.endswith("💖💖💖")


def test_compliment_is_deterministic_with_seed():
    """Using the same seed should produce the same output."""
    a = compliment(role="designer", mood="cheeky", seed=42)
    b = compliment(role="designer", mood="cheeky", seed=42)
    assert a == b


def test_compliment_differs_with_different_seeds():
    """Different seeds should generally give different compliments."""
    a = compliment(role="designer", mood="cheeky", seed=42)
    b = compliment(role="designer", mood="cheeky", seed=43)
    assert a != b

def test_stats_shapes_and_sums():
    s = pyflirt.stats()
    assert isinstance(s, dict)
    assert "total" in s and "by_category" in s and "cheese_hist" in s
    cats = pyflirt.categories()
    assert set(s["by_category"].keys()) == set(cats)
    assert set(s["cheese_hist"].keys()) == {1, 2, 3, 4, 5}
    assert s["total"] == sum(s["by_category"].values())
    assert s["total"] == sum(s["cheese_hist"].values())

def test_search_basic_and_limit_seed():
    sample = pyflirt.line(seed=12345)
    token = ""
    for t in re.findall(r"[A-Za-z]+", sample):
        if len(t) >= 3:
            token = t
            break
    if not token:
        token = "love"

    r1 = pyflirt.search(token, limit=3, seed=7)
    r2 = pyflirt.search(token, limit=3, seed=7)
    r3 = pyflirt.search(token, limit=3, seed=8)

    assert len(r1) <= 3
    assert r1 == r2
    if len(r1) > 1 and len(r3) > 1:
        assert r1 != r3 or r1[0] != r3[0]
    tl = token.lower()
    assert all(tl in s.lower() for s in r1)

def test_search_filters_and_errors():
    token = "the"
    a = pyflirt.search(token, cheese=1, limit=50, seed=1)
    b = pyflirt.search(token, cheese=5, limit=50, seed=1)
    assert len(a) <= len(b)
    try:
        pyflirt.search("x", category="__nope__", limit=1)
        ok = False
    except ValueError:
        ok = True
    assert ok

    try:
        pyflirt.search("", limit=1)
        ok = False
    except ValueError:
        ok = True
    assert ok

