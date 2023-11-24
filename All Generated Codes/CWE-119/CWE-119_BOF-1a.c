#include <stdio.h>
#include <string.h>

void copyBytes(void *dest, const void *src, size_t numBytes) {
    if (numBytes <= 256) {
        memcpy(dest, src, numBytes);
        printf("Copied %zu bytes from source to destination.\n", numBytes);
    } else {
        printf("Error: Number of bytes to copy exceeds the buffer size (256 bytes).\n");
    }
}

int main() {
    char source[256];      // Source memory location
    char destination[256]; // Destination memory location
    size_t numBytes = 100; // Number of bytes to copy

    // Call the copyBytes function to copy data
    copyBytes(destination, source, numBytes);

    return 0;
}
