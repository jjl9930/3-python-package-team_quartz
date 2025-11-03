import pytest
from pyflirt import compliment


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
