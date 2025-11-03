"""
core.py — core logic for pyflirt 💘

Currently includes:
- compliment(): generate a developer-themed compliment
"""

import random


__all__ = ["compliment"]


def compliment(role="developer", mood="sweet", name=None, emojis=0, seed=None):
    """
    Generate a developer-themed compliment.

    Args:
        role (str): One of ["developer", "designer", "manager", "data"].
        mood (str): One of ["sweet", "cheeky", "nerdy"].
        name (str, optional): Person's name to personalize.
        emojis (int): Number of 💖 emojis to append.
        seed (int, optional): Random seed for deterministic selection.

    Returns:
        str: A playful compliment string.
    """
    rng = random.Random(seed) if seed is not None else random

    templates = {
        "developer": {
            "sweet": [
                "Your code is cleaner than a freshly cloned repo{name_bit}",
                "You commit kindness with every push{name_bit}",
                "You’re the pull request everyone approves instantly{name_bit}",
            ],
            "cheeky": [
                "You refactor hearts, not just code{name_bit}",
                "You’ve got more charm than a recursive function{name_bit}",
                "You must be a keyboard shortcut—because you’re my type{name_bit}",
            ],
            "nerdy": [
                "You debug my sadness faster than VSCode{name_bit}",
                "You’re the semicolon that completes my statement{name_bit}",
                "If beauty were an algorithm, you’d be O(1){name_bit}",
            ],
        },
        "designer": {
            "sweet": [
                "Your aesthetic sense brightens every UI{name_bit}",
                "You bring color theory to my grayscale days{name_bit}",
                "Pixels align themselves just to please you{name_bit}",
            ],
            "cheeky": [
                "You must be a vector—because you’ve got direction{name_bit}",
                "Are you a grid system? Because my heart is well-aligned{name_bit}",
                "You kerningly complete me{name_bit}",
            ],
            "nerdy": [
                "You optimize whitespace like a legend{name_bit}",
                "Your Figma files are pure poetry{name_bit}",
                "Even Helvetica blushes when you walk in{name_bit}",
            ],
        },
        "manager": {
            "sweet": [
                "You lead with empathy{name_bit}",
                "Your standups make Mondays bearable{name_bit}",
                "You’re the reason meetings actually end early{name_bit}",
            ],
            "cheeky": [
                "You manage hearts better than timelines{name_bit}",
                "You’re my favorite deliverable{name_bit}",
                "You’ve got more charisma than a sprint demo{name_bit}",
            ],
            "nerdy": [
                "You allocate my attention like a well-balanced backlog{name_bit}",
                "KPIs envy your energy{name_bit}",
                "Your OKRs? Outrageously Kind & Radiant{name_bit}",
            ],
        },
        "data": {
            "sweet": [
                "You turn noise into beauty{name_bit}",
                "Every dataset wishes it were as clean as your heart{name_bit}",
                "You make outliers feel included{name_bit}",
            ],
            "cheeky": [
                "You must be a correlation—because you complete my regression{name_bit}",
                "You’re my favorite variable{name_bit}",
                "You pivot-table my emotions{name_bit}",
            ],
            "nerdy": [
                "Your confidence interval? 100%{name_bit}",
                "You’re statistically significant in my life{name_bit}",
                "Your curves fit any model{name_bit}",
            ],
        },
    }

    # Normalize and validate
    role = role.lower()
    mood = mood.lower()
    if role not in templates:
        raise ValueError(f"Unknown role '{role}'. Choose from {list(templates.keys())}.")
    if mood not in templates[role]:
        raise ValueError(f"Unknown mood '{mood}'. Choose from {list(templates[role].keys())}.")

    # Select random compliment
    template = rng.choice(templates[role][mood])
    name_bit = f", {name}" if name else ""
    compliment_text = template.format(name_bit=name_bit)

    # Add emojis if requested
    if emojis > 0:
        compliment_text += " " + "💖" * emojis

    return compliment_text
