def convert(text):
    """
    Convert :) to 🙂 and :( to 🙁 in the given text.

    Parameters:
    text (str): The input text to be converted.

    Returns:
    str: The converted text.
    """
    # Replace :) with 🙂 and :( with 🙁
    converted_text = text.replace(":)", "🙂").replace(":(", "🙁")
    return converted_text

def main():
    """
    Prompt the user for input, call the convert function on it, and print the result.
    """
    # Prompt the user for input
    user_input = input("Enter text: ")
    # Convert the input and print the result
    print(convert(user_input))

# Call main function
CS50P/faces/faces.py
