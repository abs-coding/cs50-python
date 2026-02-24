def main() -> None:
    """Main part of the program"""
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time: str) -> float:
    """Return the given time (#:## or ##:##) into a float"""
    hours, minutes = time.split(":")
    return int(hours) + (int(minutes) / 60)


if __name__ == "__main__":
    main()
