def main() -> None:
    """Main part of the program"""
    possible_answers = ["42", "forty two", "forty-two"]

    answer = input(
        "What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

    if answer in possible_answers:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
