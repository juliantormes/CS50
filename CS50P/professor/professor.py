import random

def main():
    # Get the level from the user
    level = get_level()
    score = 0

    # Loop through 10 math problems
    for i in range(10):
        # Generate two random integers based on the level
        x, y = generate_integer(level), generate_integer(level)
        answer = x + y
        tries = 0

        # Print the problem and await user's input on the same line
        print(f"Problem {i+1}: {x} + {y} = ", end="")

        # Allow up to three attempts for each problem
        while tries < 3:
            try:
                # Check user's input against the correct answer
                user_input = int(input())
                if user_input == answer:
                    score += 1
                    print("Correct!")
                    break
                else:
                    # Incorrect answer handling
                    print("EEE")
                    if tries < 2:
                        # Prompt the user to try again for the same problem
                        print(f"Try again: {x} + {y} = ", end="")
                    tries += 1
            except ValueError:
                # Handle non-integer inputs
                print("EEE")
                if tries < 2:
                    # Prompt for retry on invalid input
                    print(f"Try again: {x} + {y} = ", end="")
                tries += 1

        # Provide the correct answer after three failed attempts
        if tries == 3:
            print(f"The correct answer was {answer}")

    # Display the user's final score
    print(f"Your final score: {score} out of 10")

def get_level():
    # Continuously prompt for level until a valid one is entered
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    # Generate a random integer based on the level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        # Raise an error for invalid level
        raise ValueError("Level must be 1, 2, or 3")

if __name__ == "__main__":
    main()
