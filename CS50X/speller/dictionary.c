// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 2927; // Prime number closer to (26^3)/6 (This is the size i get a similar performance to staff)

// Hash table
node *table[N];

// Track of the amount of words in a dictionary
int count_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
#include <ctype.h>

// I started by doing Power of 26 in the hash. But i didnt like that i have to use that many memory so i asked ChatGPT how to make a
// more balanced method and this came out (Was the only thing i used it for)
unsigned int hash(const char *word)
{
    unsigned int hash_value = 0;
    const unsigned int prime = 31; // Commonly used prime for this purpose
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash_value = hash_value * prime + (toupper(word[i]) - 'A');
    }
    return hash_value % N; // Modulo operation ensures it fits in table
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open Dictionary File
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fclose(file);
        return false;
    }
    // Read Strings from File
    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // Create a New Node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false;
        }
        strcpy(n->word, buffer);
        n->next = NULL;

        // Hash Word

        int index = hash(buffer);

        // Insert Node into Hash Table
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }
        count_words++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *cursor;
    node *tmp;
    for (int i = 0; i < N; i++)
    {
        cursor = table[i];
        tmp = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
