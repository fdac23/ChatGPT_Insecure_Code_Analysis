#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <buffer_size>\n", argv[0]);
        return 1; // Return an error code
    }

    int buffer_size = atoi(argv[1]); // Convert the argument to an integer

    if (buffer_size <= 0) {
        fprintf(stderr, "Buffer size must be a positive integer.\n");
        return 1; // Return an error code
    }

    // Allocate the buffer
    char *buffer = (char *)malloc(buffer_size);
    if (buffer == NULL) {
        fprintf(stderr, "Failed to allocate memory for the buffer.\n");
        return 1; // Return an error code
    }

    // Print the contents of the buffer (initially uninitialized)
    printf("Buffer contents:\n%s\n", buffer);

    // Free the allocated memory
    free(buffer);

    return 0; // Return a success code
}