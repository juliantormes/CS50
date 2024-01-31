#include <cs50.h>
#include <stdio.h>
int main(void)
{
    long int cc;
    int digit_count = 0;
    int sum = 0;
    int FirstDigits = 0;

    // Get Credit card number

    do
    {
        cc = get_long("Number: ");
    }
    while (cc < 1);

    // checksum
    while (cc > 0)
    {
        int digit = cc % 10;
        cc /= 10;
        digit_count++;
        if (cc < 100 && cc > 10)
        {
            FirstDigits = cc;
        }

        if (digit_count % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
                digit -= 9;
            }
        }

        sum += digit;
    }
    // Check length and starting digits
    if (sum % 10 == 0)
    {
        if (digit_count == 15 && (FirstDigits == 34 || FirstDigits == 37))
        {
            printf("AMEX\n");
        }
        else if (digit_count == 16 && (FirstDigits >= 51 && FirstDigits <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((FirstDigits / 10) % 10 == 4 && digit_count >= 13 && digit_count <= 16)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}