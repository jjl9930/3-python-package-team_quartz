"""
pyflirt 💘

APIs:
- line(category, name, cheese, seed)
- lines(n, categories, name, cheese, seed)
- compliment(role, mood, name, emojis, seed)
- rate_line(text, metric, seed)
"""

from .core import ( 
    compliment,
)

__all__ = [
    "compliment",

]

__version__ = "0.1.0"
