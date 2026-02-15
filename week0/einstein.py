def main():
    """Main part of the program"""
    c = 300_000_000
    mass = int(input("m: "))
    energy = mass * pow(c, 2)
    print(energy)


if __name__ == "__main__":
    main()
