import string


def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    # Split the text by spaces and count the number of items
    words = text.split()
    return len(words)


def count_sentences(text):
    count = 0
    for char in text:
        if char in [".", "?", "!"]:
            count += 1
    return count


def main():
    # Prompt the user for text
    text = input("Text: ")

    # Count the number of letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    # Grade = 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words, and S is the average number of sentences per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")


if __name__ == "__main__":
    main()
