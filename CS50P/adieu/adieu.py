def get_names():
    # Create an empty list to store names
    names = []
    print("Enter names (Ctrl-D to finish):")
    while True:
        try:
            # Read a name from the user
            name = input()
            names.append(name)
        except EOFError:
            # Break the loop if an EOF (End Of File) is encountered (Ctrl-D)
            break
    return names

def format_farewell(names):
    # Check the number of names and format the farewell message accordingly
    if len(names) == 1:
        # Single name, so no need for commas or 'and'
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        # Two names, separated by 'and'
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        # More than two names, separate with commas and 'and' before the last name
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

def main():
    # Retrieve the list of names from the user
    names = get_names()
    # Format the farewell message
    farewell_message = format_farewell(names)
    # Print the formatted farewell message
    print(farewell_message)

if __name__ == "__main__":
    # Entry point of the program
    main()
