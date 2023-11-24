#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int size = 10;

    // Allocate memory for the first chunk
    int* chunk1 = (int*)malloc(size * sizeof(int));
    if (chunk1 == NULL) {
        perror("malloc");
        return 1;
    }

    // Initialize the first chunk with some values
    for (int i = 0; i < size; i++) {
        chunk1[i] = i * 2;
    }

    // Allocate memory for the second chunk
    int* chunk2 = (int*)malloc(size * sizeof(int));
    if (chunk2 == NULL) {
        perror("malloc");
        free(chunk1);
        return 1;
    }

    // Copy the contents of the first chunk into the second chunk
    memcpy(chunk2, chunk1, size * sizeof(int));

    // Print the contents of the second chunk
    printf("Contents of the second chunk after copying:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", chunk2[i]);
    }
    printf("\n");

    // Free the memory allocated to the first chunk
    free(chunk1);

    // Print the contents of the second chunk after freeing the first chunk
    printf("Contents of the second chunk after freeing the first chunk:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", chunk2[i]);
    }
    printf("\n");

    // Free the memory allocated to the second chunk
    free(chunk2);

    return 0;
}