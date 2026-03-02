def main():
    """Main part of the program"""
    PRICE = 50
    DENOMINATIONS = [5, 10, 25]
    given_amount = 0

    # Calculate the Due amount until the given amount is less than 50
    while given_amount < 50:
        amount = int(input("Amount: "))

        if amount in DENOMINATIONS:
            given_amount += amount

        if given_amount < 50:
            print(f"Amount Due: {PRICE - given_amount}")
        else:
            print(f"Amount Due: ", 0)

    print(f"Change owed: {given_amount - PRICE}")


if __name__ == "__main__":
    main()
