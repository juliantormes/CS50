def main():
    text = input("Input: ")
    output_text = shorten(text)
    print("Output:", output_text)
    
def shorten(word):
    # Define a string of vowels to be removed
    vowels = "aeiouAEIOU"
    # Initialize an empty string for the result
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result
if __name__ == "__main__":
    main()
