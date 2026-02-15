def main() -> None:
    """Main part of the program"""
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """Convert dollars $##.## (str) into float"""
    return float(d.replace("$", ""))


def percent_to_float(p: str) -> float:
    """Convert percentage ##% (str) into float"""
    return float(p.replace("%", "")) / 100


if __name__ == "__main__":
    main()
