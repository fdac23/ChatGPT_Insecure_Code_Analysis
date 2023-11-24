#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int size = 10;
    int* first_chunk = (int*)malloc(size * sizeof(int));
    int* second_chunk = (int*)malloc(size * sizeof(int));

    // Check if memory allocation was successful
    if (first_chunk == NULL || second_chunk == NULL) {
        perror("Memory allocation failed");
        return 1;
    }

    // Initialize the first chunk
    for (int i = 0; i < size; i++) {
        first_chunk[i] = i;
    }

    // Copy the contents of the first chunk to the second chunk
    memcpy(second_chunk, first_chunk, size * sizeof(int));

    // Free the first chunk
    free(first_chunk);
    first_chunk = NULL;

    // Free the second chunk
    free(second_chunk);
    second_chunk = NULL;

    return 0;
}