#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text, int length);
int count_words(string textn, int length);
int count_sentences(string text, int length);

int main(void)
{
    // Make the user prompt for text
    string text = get_string("Text: ");
    int length = strlen(text);

    // Count the number of letters, words, and sentences
    int letters = count_letters(text, length);
    int words = count_words(text, length);
    int sentences = count_sentences(text, length);

    //printf("Letters: %i\n", letters);

    //printf("Words: %i\n", words);

    //printf("Sentences: %i\n", sentences);

    // Calculate the Coleman-Liau index (a readability formula)
    // Grade = 0.0588 * L - 0.296 * S - 15.8, where L is the average letters per 100 words, and S is the average sentences per 100 words
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    // Print the grade of the text (Round numbers, Anything below 1 is grade 1,Anything higher than 16 is grade 16)
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", index);
    }
}
// Counter the number of letters of the text
int count_letters(string text, int length)
{
    int count = 0;
    for (int i = 0; i < length; i++)
    {
        if (isupper(text[i]))
        {
            count++;
        }
        else if (islower(text[i]))
        {
            count++;
        }
    }
    return count;
}
// Counter the number of words (By blank space)
int count_words(string text, int length)
{
    int count = 1;
    for (int i = 0; i < length; i++)
    {
        if (isblank(text[i]))
        {
            count++;
        }
    }
    return count;
}
// Counter the number of sentences (By separation of "." "?" or "!")
int count_sentences(string text, int length)
{
    int count = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!') //if (ispunct(text[i]))
        {
            count++;
        }
    }
    return count;
}