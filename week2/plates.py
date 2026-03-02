def main() -> None:
    """Main part of the program"""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    """Returns True if the Plate Number is valid otherwise False"""
    return (check_character_valid(s) and check_number_valid(s))


def check_character_valid(plate: str) -> bool:
    """Check if the characters in the Vanity Plate follows the required rules"""
    return (plate.isalnum() and plate[0:2].isalpha() and 2 <= len(plate) <= 6)


def check_number_valid(plate: str) -> bool:
    """Check if the number in the Vanity Plate follows the required rules"""
    for i in plate:
        if i.isdigit():
            num_position = plate.find(i)

            if plate[num_position] == "0" or (not plate[num_position:].isdigit()):
                return False
            break

    return True


if __name__ == "__main__":
    main()
