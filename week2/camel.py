def main():
    """Main part of the program"""
    camel_case_variable = input("camelCase: ")
    print(snake_case_converter(camel_case_variable))


def snake_case_converter(camel_case_text: str) -> str:
    """Returns the text (camle case) in snake case"""
    snake_case_text = ""

    for char in camel_case_text:
        if char.isupper():
            snake_case_text += f"_{char.lower()}"
        else:
            snake_case_text += char

    return snake_case_text


if __name__ == "__main__":
    main()
