# Import the emoji module to use its functionalities
import emoji

def emojize_string():
    user_input = input()
    # Convert any emoji codes in the string to emojis
    # The language='alias' argument specifies that we are using emoji aliases
    emojized = emoji.emojize(user_input, language='alias')
    print(emojized)

def main():
    emojize_string()

if __name__ == "__main__":
    main()
