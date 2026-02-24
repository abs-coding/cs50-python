def main() -> None:
    """Main part of the program"""
    greetings = input("Greeting: ").lower().strip()
    calculate_reward(greetings)


def calculate_reward(greetings: str) -> None:
    """Calculate the reward for the customer on the basis of greeting"""
    if greetings.startswith("hello"):
        print("$0")
    elif greetings.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
