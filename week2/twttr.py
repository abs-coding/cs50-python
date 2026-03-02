def main():
    """Main part of the program"""
    VOWELS = "aeiou"
    text = input("Text: ")

    for char in text:
        if char.lower() not in VOWELS:
            print(char, end="")
    print()


if __name__ == "__main__":
    main()
