def main():
    """Main part of the program"""
    grocery_items = {}

    while True:
        try:
            grocery_item = input().lower().strip()
        except EOFError:
            print("")
            break

        # set the value equal to one if the input grocery item is not on the list otherwise increment by one
        grocery_items[grocery_item] = grocery_items.get(grocery_item, 0) + 1

    for item, quantity in sorted(grocery_items.items()):
        print(quantity, item.upper())


if __name__ == "__main__":
    main()
