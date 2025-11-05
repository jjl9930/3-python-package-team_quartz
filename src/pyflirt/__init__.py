# src/pyflirt/__init__.py
"""
pyflirt 💘
Public API:
- categories()
- line(category, name, cheese, seed)
- lines(n, category, name, cheese, seed)
- compliment(role, mood, name, emojis, seed)
"""
from .api import categories, line, lines, compliment

__all__ = ["categories", "line", "lines", "compliment"]
__version__ = "0.1.0"
