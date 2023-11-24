#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Allocate two chunks of memory, each of size 10
    size_t size = 10;
    char* chunk1 = (char*)malloc(size);
    char* chunk2 = (char*)malloc(size);

    if (chunk1 == NULL || chunk2 == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    // Fill the first chunk with some data (e.g., a string)
    strncpy(chunk1, "Hello", size);

    // Copy the contents of the first chunk into the second chunk
    strncpy(chunk2, chunk1, size);

    // Print the contents of the second chunk
    printf("Contents of the second chunk: %s\n", chunk2);

    // Free the allocated memory
    free(chunk1);
    free(chunk2);

    return 0;
}
