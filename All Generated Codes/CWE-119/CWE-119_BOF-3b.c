#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if at least one argument (the program name) is provided
    if (argc < 2) {
        printf("Usage: %s <integer1> <integer2> ...\n", argv[0]);
        return 1;
    }

    // Loop through the command-line arguments and convert them to integers
    for (int i = 1; i < argc; i++) {
        int value = atoi(argv[i]);

        // Check if the conversion was successful
        if (value != 0 || (value == 0 && argv[i][0] == '0')) {
            printf("Argument %d: %d\n", i, value);
        } else {
            printf("Argument %d: Invalid input - not an integer.\n", i);
        }
    }

    return 0;
}