def camel_to_snake(text):
    """
    Convert a camelCase string to a snake_case string.

    Args:
    text (str): A string in camelCase format.

    Returns:
    str: The converted string in snake_case format.
    """
    result = ""
    for c in text:
        if c.isupper():
            # Add an underscore before an uppercase character,
            # unless it's the first character, and convert to lowercase.
            if result:
                result += "_"
            result += c.lower()
        else:
            # Directly append lowercase characters.
            result += c
    return result

def main():
    """
    Main function to take user input and convert it from camelCase to snake_case.
    """
    camel = input("Enter a camelCase string: ")
    snake = camel_to_snake(camel)
    print("Converted to snake_case:", snake)

if __name__ == "__main__":
    main()
