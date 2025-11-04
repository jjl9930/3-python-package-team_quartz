from pyflirt import line, lines, categories
import pytest
from pyflirt import compliment
from pyflirt import rate_line



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

def test_rate_line_length():
    short_line = "Hi!"
    long_line = "This is a really long pickup line that could be annoying."
    assert rate_line(short_line, metric="length") > rate_line(long_line, metric="length")

def test_rate_line_cheese_level():
    cheesy = "You have a sweet heart."
    bland = "Hello."
    assert rate_line(cheesy, metric="cheese_level") > rate_line(bland, metric="cheese_level")

def test_rate_line_random_seed():
    r1 = rate_line("Test", metric="random", seed=42)
    r2 = rate_line("Test", metric="random", seed=42)
    r3 = rate_line("Test", metric="random", seed=43)
    assert r1 == r2
    assert r1 != r3

def test_rate_line_invalid_metric():
    with pytest.raises(ValueError):
        rate_line("test", metric="unknown")
