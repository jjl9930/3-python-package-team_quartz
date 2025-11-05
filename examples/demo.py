from pyflirt import (
    line,
    lines,
    categories,
    compliment,
    search,
    stats,
    stylize,
    say,
    rate_line,
    rainbow,
    ascii_heart,
)

def main():
    print("== categories() ==")
    cats = categories()
    print(cats)

    cat = "nerdy" if "nerdy" in cats else (cats[0] if cats else None)

    print("\n== line() ==")
    print(line(category=cat or "nerdy", name="Alex", cheese=3, seed=1))

    print("\n== lines() ==")
    for s in lines(n=3, category=cat, name="Sam", cheese=3, seed=2):
        print("-", s)

    print("\n== compliment() ==")
    print(compliment(role="developer", mood="sweet", name="Jamie", emojis=2, seed=3))

    print("\n== search() ==")
    for h in search(query="you", limit=5, seed=4):
        print("-", h)

    print("\n== stats() ==")
    st = stats()
    print("total:", st["total"])
    print("by_category:", st["by_category"])
    print("cheese_hist:", st["cheese_hist"])

    print("\n== stylize() ==")
    sample = line(category=cat or "nerdy", seed=5)
    styled = stylize(sample, width=20, uppercase=True, color="none")
    print(styled)

    print("\n== say() ==")
    # say() prints the formatted line and returns it
    returned = say(category=cat or "nerdy", seed=6, width=18, emojis=1, color="none")
    print("(returned)", returned)

    print("\n== rate_line() ==")
    txt = line(category=cat or "nerdy", seed=7)
    print("text:", txt)
    print("length score:", rate_line(txt, metric="length"))
    print("cheese score:", rate_line(txt, metric="cheese_level"))
    print("random score (seeded):", rate_line(txt, metric="random", seed=42))

    print("\n== rainbow() ==")
    rainbow_text = rainbow("You brighten up my terminal 💻💘")
    print(rainbow_text)

    print("\n== ascii_heart() ==")
    print(ascii_heart())


if __name__ == "__main__":
    main()
