MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main() -> None:
    """Main part of the program"""
    date = get_valid_date()
    print_iso_format_date(*date)


def get_valid_date() -> tuple[int]:
    """Get the valid date from the user and returns day, month and year"""
    while True:
        user_date = input("Date: ").strip()
        try:
            if "/" in user_date:
                month, day, year = user_date.split("/")
                month, day, year = int(month), int(day), int(year)
            elif "," in user_date:
                month, day, year = user_date.split(" ")
                month = MONTHS.index(month) + 1
                day, year = int(day.replace(",", "")), int(year)
            else:
                continue
        except ValueError:
            continue

        if day <= 31 and month <= 12:
            return day, month, year


def print_iso_format_date(day: int, month: int, year: int) -> None:
    """Prints the date in the iso format (YYYY-MM-DD)"""
    print(f"{year}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()
