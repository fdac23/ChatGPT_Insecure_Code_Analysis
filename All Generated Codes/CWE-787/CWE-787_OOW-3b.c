#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if exactly one argument is provided
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <argument>\n", argv[0]);
        exit(1);
    }

    // Get the argument from the command line
    char *input = argv[1];

    // Print the original argument
    printf("Original Argument: %s\n", input);

    // Trim trailing whitespace (newline characters)
    size_t len = strlen(input);
    while (len > 0 && (input[len - 1] == '\n' || input[len - 1] == '\r')) {
        input[len - 1] = '\0';
        len--;
    }

    // Print the trimmed argument
    printf("Trimmed Argument: %s\n", input);

    // Exit the program
    return 0;
}