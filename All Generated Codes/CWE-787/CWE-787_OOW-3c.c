#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to trim trailing whitespace characters from a string
void trimTrailingWhitespace(char *str) {
    int length = strlen(str);

    // Start from the end of the string and move backwards
    while (length > 0 && isspace(str[length - 1])) {
        str[length - 1] = '\0'; // Replace whitespace with null character
        length--;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <argument>\n", argv[0]);
        return 1;
    }

    char *input = argv[1];

    // Trim trailing whitespace characters
    trimTrailingWhitespace(input);

    // Print the modified argument
    printf("Modified Argument: \"%s\"\n", input);

    return 0;
}