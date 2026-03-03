def main():
    """Main part of the program"""
    result = calculate_fuel_percentage()

    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{round(result)}%")


def calculate_fuel_percentage() -> float:
    """Calculate the fuel percentage according to the given fraction"""
    while True:
        fuel_fraction = input("Fraction: ")

        # Raises value error if the the numerator or denominator is not int
        try:
            numerator, denominator = fuel_fraction.split("/")
            numerator, denominator = int(numerator), int(denominator)
            result = numerator / denominator * 100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            # Ensures that the numerator and denomibator are valid
            if numerator <= denominator and numerator >= 0:
                return result


if __name__ == "__main__":
    main()
