from pyflirt import line, lines, categories, compliment, search, stats

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

if __name__ == "__main__":
    main()
