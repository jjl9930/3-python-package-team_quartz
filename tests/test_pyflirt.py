import pytest
from pyflirt import categories, line, lines, compliment

def test_categories_sorted_and_nonempty():
    cats = categories()
    assert cats == sorted(cats)
    assert len(cats) > 0

def test_categories_reflect_bank_contents():
    # If BANK has "nerdy" in data, ensure it's present
    assert "nerdy" in categories()

def test_line_invalid_cheese_raises():
    with pytest.raises(ValueError):
        line(cheese=0)
    with pytest.raises(ValueError):
        line(cheese=6)

def test_line_unknown_category_raises():
    with pytest.raises(ValueError):
        line(category="not-a-cat")

def test_lines_n_zero_returns_empty():
    assert lines(n=0) == []

def test_lines_invalid_cheese_raises():
    with pytest.raises(ValueError):
        lines(cheese=99)

def test_compliment_invalid_role_raises():
    with pytest.raises(ValueError):
        compliment(role="astronaut")

def test_compliment_invalid_mood_raises():
    with pytest.raises(ValueError):
        compliment(role="developer", mood="salty")

def test_compliment_emojis_appended():
    base = compliment(role="developer", mood="sweet", emojis=3, seed=1)
    assert base.endswith("💖💖💖")
