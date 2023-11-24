#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Seed the random number generator with the current time
    srand(time(NULL));

    // Generate three random floating-point numbers
    float random_float1 = (float)rand() / RAND_MAX;
    float random_float2 = (float)rand() / RAND_MAX;
    float random_float3 = (float)rand() / RAND_MAX;

    // Convert the random floats to strings
    char string[32];
    char string2[32];
    char string3[32];

    sprintf(string, "%.6f", random_float1);
    sprintf(string2, "%.6f", random_float2);
    sprintf(string3, "%.6f", random_float3);

    // Print the generated random strings
    printf("Random Float 1: %s\n", string);
    printf("Random Float 2: %s\n", string2);
    printf("Random Float 3: %s\n", string3);

    return 0;
}