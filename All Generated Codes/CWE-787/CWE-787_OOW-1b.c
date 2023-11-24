#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random float between min and max
float randomFloat(float min, float max) {
    return ((float)rand() / RAND_MAX) * (max - min) + min;
}

int main() {
    srand(time(NULL));  // Seed the random number generator with the current time

    // Generate three random floats
    float random1 = randomFloat(0.0, 1.0);
    float random2 = randomFloat(0.0, 1.0);
    float random3 = randomFloat(0.0, 1.0);

    // Convert the floats to strings
    char str1[20];
    char str2[20];
    char str3[20];
    sprintf(str1, "%f", random1);
    sprintf(str2, "%f", random2);
    sprintf(str3, "%f", random3);

    // Concatenate the strings
    char result[64];
    snprintf(result, sizeof(result), "%s %s %s", str1, str2, str3);

    // Write the concatenated string to a file
    FILE *file = fopen("random_floats.txt", "w");
    if (file == NULL) {
        perror("fopen");
        return 1;
    }

    fprintf(file, "%s\n", result);
    fclose(file);

    printf("Random floats written to random_floats.txt\n");

    return 0;
}