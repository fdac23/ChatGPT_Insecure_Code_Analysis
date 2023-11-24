#include <stdio.h>
#include <stdlib.h>

int main() {
    size_t buffer_size = 1024; // Specify the size of the buffer

    // Allocate memory for the buffer
    char *buffer = (char *)malloc(buffer_size);

    if (buffer == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1; // Exit with an error code
    }

    // Free the buffer in a loop (example with three iterations)
    for (int i = 0; i < 3; i++) {
        free(buffer);
        printf("Buffer freed in iteration %d\n", i + 1);
    }

    return 0; // Exit with success
}