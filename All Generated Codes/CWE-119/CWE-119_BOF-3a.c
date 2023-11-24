#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if there are at least three command line arguments
    if (argc < 3) {
        printf("Usage: %s <index> <arg1> <arg2> ... <argN>\n", argv[0]);
        return 1; // Exit with an error code
    }

    // Get the index from the second command line argument
    int index = atoi(argv[1]);

    // Check if the index is within a valid range
    if (index < 2 || index >= argc) {
        printf("Invalid index. Please enter an index between 2 and %d.\n", argc - 1);
        return 1; // Exit with an error code
    }

    // Print the argument at the specified index
    printf("Argument at index %d: %s\n", index, argv[index]);

    return 0; // Exit the program
}
