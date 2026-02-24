def main() -> None:
    """Main part of the program"""
    expression = input("Expression: ")
    print(calculator(expression))


def calculator(expression: str) -> float:
    """Calculates the given arithematic expression"""
    num_1, operator, num_2 = expression.split(" ")
    num_1, num_2 = float(num_1), float(num_2)

    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        return num_1 / num_2


if __name__ == "__main__":
    main()
