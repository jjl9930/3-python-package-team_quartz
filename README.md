# pyflirt

A Python package that gives you developer-themed pickup lines and compliments. Because coding should be fun.

## What is this?

This package has a collection of cheesy (but configurable) pickup lines and compliments for developers, designers, managers, and data scientists. You can get random lines, filter by category, adjust the cheesiness level, and customize compliments.

## Installation

```bash
pip install pyflirt
```

## Quick Start

```python
from pyflirt import line, lines, compliment, categories

# Get one random pickup line
print(line())

# Get a line in a specific category
print(line(category="nerdy"))

# Get multiple lines
print(lines(n=5, category="cs"))

# Get a compliment
print(compliment(role="developer", mood="sweet"))
```

## Functions

### `line(category="nerdy", name=None, cheese=2, seed=None)`

Returns one random pickup line.

- `category`: Pick a category like "nerdy", "cs", "math", "poetic", or "classic". Default is "nerdy".
- `name`: If the line supports it, this name will be inserted.
- `cheese`: How cheesy should it be? 1 (least cheesy) to 5 (very cheesy). Default is 2.
- `seed`: Optional number for reproducible results.

Example:
```python
line(category="cs", name="Alex", cheese=2)
```

### `lines(n=5, category=None, name=None, cheese=2, seed=None)`

Returns a list of pickup lines.

- `n`: How many lines you want.
- Other parameters work the same as `line()`.

Example:
```python
lines(n=3, category="math", cheese=3)
```

### `compliment(role="developer", mood="sweet", name=None, emojis=0, seed=None)`

Returns a compliment for a specific role.

- `role`: Choose from "developer", "designer", "manager", or "data".
- `mood`: "sweet", "cheeky", or "nerdy".
- `name`: Optional name to include in the compliment.
- `emojis`: Number of heart emojis to add (0-5).
- `seed`: Optional number for reproducible results.

Example:
```python
compliment(role="designer", mood="cheeky", name="Sam", emojis=2)
```

### `categories()`

Returns a list of all available pickup line categories.

Example:
```python
print(categories())
# ['classic', 'cs', 'math', 'nerdy', 'poetic']
```

## Development Setup

If you want to work on this package:

1. Clone the repo:
```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_quartz.git
cd 3-python-package-team_quartz
```

2. Install pipenv (if you don't have it):
```bash
pip install pipenv
```

3. Install dependencies:
```bash
pipenv install --dev
```

4. Activate the virtual environment:
```bash
pipenv shell
```

5. Run tests:
```bash
pytest
```

6. Build the package:
```bash
python -m build
```

## Links

- [PyPI Package](https://pypi.org/project/pyflirt/)
- [GitHub Repository](https://github.com/swe-students-fall2025/3-python-package-team_quartz)

## Contributors

See the [contributors page](https://github.com/swe-students-fall2025/3-python-package-team_quartz/graphs/contributors) for a list of everyone who worked on this project.
