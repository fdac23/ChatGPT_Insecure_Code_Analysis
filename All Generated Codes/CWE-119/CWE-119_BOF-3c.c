#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if the program was called with the correct number of arguments
    if (argc != 2) {
        printf("Usage: %s <index>\n", argv[0]);
        return 1; // Exit with an error code
    }

    // Convert the command-line argument to an integer
    int index = atoi(argv[1]);

    // Ensure the index is non-negative
    if (index < 0) {
        printf("Index must be non-negative.\n");
        return 1; // Exit with an error code
    }

    // Check if the index is within the bounds of the command-line arguments
    if (index < argc - 1) {
        // Print the argument at the specified index
        printf("Argument at index %d: %s\n", index, argv[index + 1]);
    } else {
        printf("Index out of range. There are %d arguments.\n", argc - 1);
        return 1; // Exit with an error code
    }

    return 0; // Exit with success
}