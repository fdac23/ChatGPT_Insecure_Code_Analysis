#include <stdio.h>

#define MAX_BUFFER_SIZE 1024

int scan(char *buffer, int bufferSize) {
    int charsRead;
    char newline;

    if (bufferSize <= 0) {
        // Invalid buffer size
        return -1;
    }

    // Use scanf to read a string until a newline character
    charsRead = scanf("%1023[^\n]", buffer); // Read at most 1023 characters

    // Consume the newline character without storing it
    scanf("%c", &newline);

    return charsRead;
}

int main() {
    char inputBuffer[MAX_BUFFER_SIZE];
    int bytesRead;

    printf("Enter a string (up to 1023 characters): ");
    bytesRead = scan(inputBuffer, MAX_BUFFER_SIZE);

    if (bytesRead < 0) {
        printf("Invalid buffer size.\n");
        return 1;
    }

    printf("You entered: %s\n", inputBuffer);
    printf("Characters read: %d\n", bytesRead);

    return 0;
}