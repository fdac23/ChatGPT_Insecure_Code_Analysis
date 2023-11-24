#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <string_argument>\n", argv[0]);
        return 1;
    }

    // Check the argument to make sure it is a string
    const char* inputString = argv[1];

    // Remove trailing whitespace
    int length = strlen(inputString);
    while (length > 0 && isspace(inputString[length - 1])) {
        inputString[--length] = '\0';
    }

    // Remove newlines
    for (int i = 0; inputString[i]; i++) {
        if (inputString[i] == '\n') {
            inputString[i] = '\0';
            break;
        }
    }

    // Now, inputString contains the trimmed string
    printf("Trimmed String: %s\n", inputString);

    return 0;
}
