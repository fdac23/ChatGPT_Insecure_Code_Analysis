#include <stdio.h>
#include <string.h>

// Function to copy a specified number of bytes from source to destination
void copyBytes(void *dest, const void *src, size_t numBytes) {
    // Using memcpy to copy 'numBytes' bytes from 'src' to 'dest'
    memcpy(dest, src, numBytes);
}

// Function to calculate the length of a string and copy it to a buffer
size_t stringLengthAndCopy(char *buffer, const char *str) {
    // Calculate the length of the input string
    size_t length = strlen(str);
    
    // Copy the string to the provided buffer
    strcpy(buffer, str);

    // Return the length of the string
    return length;
}

int main() {
    // Example usage:
    char source[] = "Hello, World!";
    char destination[20];
    char buffer[50];
    
    // Copy 7 bytes from source to destination
    copyBytes(destination, source, 7);
    
    // Calculate the length of the string and copy it to a buffer
    size_t length = stringLengthAndCopy(buffer, source);
    
    printf("Copied Bytes: %s\n", destination);
    printf("String Length: %zu\n", length);
    printf("Copied String: %s\n", buffer);
    
    return 0;
}