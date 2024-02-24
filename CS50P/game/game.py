import random

def get_positive_integer(prompt):
    """Prompt the user for a positive integer and return it."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Prompt the user for the level N
    N = get_positive_integer("Enter a level (positive integer): ")

    # Generate a random integer between 1 and N
    secret_number = random.randint(1, N)

    # Prompt the user to guess the integer
    while True:
        guess = get_positive_integer("Guess the integer: ")

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
