#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 512
#define NAME_SIZE 8

typedef uint8_t BYTE;

// Function to check if buffer starts with a JPEG signature
int is_jpeg_header(BYTE buffer[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    char *input_filename = argv[1];
    FILE *input_file = fopen(input_filename, "r");
    if (input_file == NULL)
    {
        printf("Could not open file: %s\n", input_filename);
        return 1;
    }

    int file_number = 0;
    FILE *output_file = NULL;
    BYTE buffer[BLOCK_SIZE];

    while (fread(buffer, BLOCK_SIZE, 1, input_file) == 1)
    {
        if (is_jpeg_header(buffer))
        {
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            char output_filename[NAME_SIZE];
            sprintf(output_filename, "%03i.jpg", file_number);
            output_file = fopen(output_filename, "w");

            if (output_file == NULL)
            {
                printf("Could not create JPEG file: %s\n", output_filename);
                fclose(input_file);
                return 1;
            }

            file_number++;
        }

        if (output_file != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, output_file);
        }
    }

    if (output_file != NULL)
    {
        fclose(output_file);
    }

    fclose(input_file);
    return 0;
}

int is_jpeg_header(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
}
