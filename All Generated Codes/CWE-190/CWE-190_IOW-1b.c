#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <value>\n", argv[0]);
        return 1;
    }

    // Convert the command-line argument to an integer
    int value = atoi(argv[1]);

    // Define the offset
    const int offset = 1000;

    // Add the offset to the value
    int result = value + offset;

    printf("Original value: %d\n", value);
    printf("Value with offset: %d\n", result);

    return 0;
}