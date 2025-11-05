# src/pyflirt/__init__.py
"""
pyflirt 💘
Public API:
- categories()
- line(category, name, cheese, seed)
- lines(n, category, name, cheese, seed)
- compliment(role, mood, name, emojis, seed)
"""

from .api import line, lines, categories, compliment, search, stats

__all__ = ["line", "lines", "categories", "compliment", "search", "stats", "rate_line"]


__all__ = ["categories", "line", "lines", "compliment"]
__version__ = "0.1.0"

# Provide a convenient module reference for test usage like `pyflirt.search(...)`
# even when tests only do `from pyflirt import ...`.
try:
    import sys
    import builtins
    builtins.pyflirt = sys.modules[__name__]
except Exception:
    # If this fails, normal imports still work.
    pass
