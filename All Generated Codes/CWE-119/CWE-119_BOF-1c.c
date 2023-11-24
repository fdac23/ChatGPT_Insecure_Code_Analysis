#include <stdio.h>
#include <string.h>

// Function to copy a specified number of bytes from source to destination
void my_memcpy(void *dest, const void *src, size_t size) {
    char *d = (char *)dest;
    const char *s = (const char *)src;

    for (size_t i = 0; i < size; i++) {
        d[i] = s[i];
    }
}

// Function to calculate the length of a string
size_t my_strlen(const char *str) {
    size_t length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

int main() {
    char buffer[10]; // Destination buffer
    const char *source = "Hello"; // Source string

    // Copy the string "Hello" to the buffer
    my_memcpy(buffer, source, my_strlen(source) + 1);

    // Print the copied string
    printf("Copied String: %s\n", buffer);

    return 0;
}