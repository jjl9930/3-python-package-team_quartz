from .core import compliment

def main():
    print("💘 Welcome to pyflirt!")
    print(compliment(role="developer", mood="cheeky", name="Alex", emojis=2))

if __name__ == "__main__":
    main()
