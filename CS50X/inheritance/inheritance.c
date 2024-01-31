#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

person *create_family(int generations)
{
    person *newPerson = malloc(sizeof(person));

    // Check if more generations are left to create
    if (generations > 1)
    {
        // Create parents for the current person
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        // Set parent pointers for the current person
        newPerson->parents[0] = parent0;
        newPerson->parents[1] = parent1;

        // Assign alleles based on parents' alleles
        newPerson->alleles[0] = parent0->alleles[rand() % 2];
        newPerson->alleles[1] = parent1->alleles[rand() % 2];
    }
    else
    {
        // Set parents to NULL if no more generations left
        newPerson->parents[0] = NULL;
        newPerson->parents[1] = NULL;

        // Randomly assign alleles for the current person
        newPerson->alleles[0] = random_allele();
        newPerson->alleles[1] = random_allele();
    }

    return newPerson;
}

void free_family(person *p)
{
    if (p == NULL)
    {
        return;
    }

    // Free parents recursively
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free current person
    free(p);
}

void print_family(person *p, int generation)
{
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person based on their generation
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}