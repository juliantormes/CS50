def casespaceinsesitivity(text):
    processed_text = ''.join([char.lower() for char in text if char.isalnum()])
    return processed_text

def main():
    """
    Prompt the user for input, call the convert function on it, and print the result.
    """
    # Prompt the user for input
    deepanswer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # Convert the input and print the result
    processed_text = casespaceinsesitivity(deepanswer)
    if processed_text == "42" or processed_text == "fortytwo" :
        print ("Yes")
    else :
        print ("No")

# Call main function
if __name__ == "__main__":
    main()
