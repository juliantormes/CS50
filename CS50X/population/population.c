#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int Initial;
    do
    {
        Initial = get_int("Initial population of llamas: ");
    }
    while (Initial < 9);
    // TODO: Prompt for end size
    int Final;
    do
    {
        Final = get_int("Final population of llamas: ");
    }
    while (Final < Initial);
    // TODO: Calculate number of years until we reach threshold
    int y;
    y = 0;
    while (Initial < Final)
    {
        Initial = Initial + (Initial / 3) - (Initial / 4);
        y = y + 1;
    }
    // TODO: Print number of years
    printf("Years: %i\n", y);
}
