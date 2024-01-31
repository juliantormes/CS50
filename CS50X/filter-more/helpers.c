#include "helpers.h"
#include <math.h>
#include <stdbool.h>
#include <string.h>
// Swap two RGB pixels
void swapRGB(RGBTRIPLE *rgb1, RGBTRIPLE *rgb2);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int sum = 0;
    double average = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sum = image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen;
            average = (double) sum / 3;
            image[i][j].rgbtRed = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // Swap the horizontally opposite pixels until the end of the left-half of the image
        for (int j = 0, k = width - 1, n = width / 2; j < n; j++, k--)
        {
            swapRGB(&image[i][j], &image[i][k]);
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0, count = 0;

            for (int dx = -1; dx <= 1; dx++)
            {
                for (int dy = -1; dy <= 1; dy++)
                {
                    int newX = i + dx, newY = j + dy;

                    if (newX >= 0 && newX < height && newY >= 0 && newY < width)
                    {
                        sumRed += image[newX][newY].rgbtRed;
                        sumGreen += image[newX][newY].rgbtGreen;
                        sumBlue += image[newX][newY].rgbtBlue;
                        count++;
                    }
                }
            }

            tmp[i][j].rgbtRed = round((double) sumRed / count);
            tmp[i][j].rgbtGreen = round((double) sumGreen / count);
            tmp[i][j].rgbtBlue = round((double) sumBlue / count);
        }
    }

    // Copy the temporary image to the real image
    memcpy(image, tmp, height * width * sizeof(RGBTRIPLE));
}

const int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
const int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

int cap_at_255(int value)
{
    return value > 255 ? 255 : value;
}

void apply_sobel(int i, int j, int height, int width, RGBTRIPLE image[height][width], RGBTRIPLE *result)
{
    int sumGx_red = 0, sumGx_green = 0, sumGx_blue = 0;
    int sumGy_red = 0, sumGy_green = 0, sumGy_blue = 0;

    for (int x = 0; x < 3; x++)
    {
        for (int y = 0; y < 3; y++)
        {
            int newX = i - 1 + x;
            int newY = j - 1 + y;

            if (newX >= 0 && newX < height && newY >= 0 && newY < width)
            {
                sumGx_red += image[newX][newY].rgbtRed * Gx[x][y];
                sumGx_green += image[newX][newY].rgbtGreen * Gx[x][y];
                sumGx_blue += image[newX][newY].rgbtBlue * Gx[x][y];

                sumGy_red += image[newX][newY].rgbtRed * Gy[x][y];
                sumGy_green += image[newX][newY].rgbtGreen * Gy[x][y];
                sumGy_blue += image[newX][newY].rgbtBlue * Gy[x][y];
            }
        }
    }

    result->rgbtRed = cap_at_255(round(sqrt(pow(sumGx_red, 2) + pow(sumGy_red, 2))));
    result->rgbtGreen = cap_at_255(round(sqrt(pow(sumGx_green, 2) + pow(sumGy_green, 2))));
    result->rgbtBlue = cap_at_255(round(sqrt(pow(sumGx_blue, 2) + pow(sumGy_blue, 2))));
}

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            apply_sobel(i, j, height, width, image, &tmp[i][j]);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = tmp[i][j];
        }
    }
}
void swapRGB(RGBTRIPLE *rgb1, RGBTRIPLE *rgb2)
{
    RGBTRIPLE tmp = *rgb1;
    *rgb1 = *rgb2;
    *rgb2 = tmp;
}