#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <value>\n", argv[0]);
        return 1; // Exit with an error code
    }

    // Convert the command-line argument to an integer
    int value = atoi(argv[1]);

    // Add 1000 to the value
    int result = value + 1000;

    // Print the result
    printf("Value after adding 1000: %d\n", result);

    return 0; // Exit with success
}