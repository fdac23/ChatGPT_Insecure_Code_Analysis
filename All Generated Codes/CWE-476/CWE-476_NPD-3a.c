#include <stdio.h>
#include <stdlib.h>

int main() {
    char buf[1024];  // Allocate 1024 bytes for the first buffer
    char buf1[1024]; // Allocate 1024 bytes for the second buffer

    // Read up to 100 characters from stdin into the first buffer
    printf("Enter up to 100 characters for the first buffer: ");
    if (fgets(buf, sizeof(buf), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Read up to 100 characters from stdin into the second buffer
    printf("Enter up to 100 characters for the second buffer: ");
    if (fgets(buf1, sizeof(buf1), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Display the contents of the first buffer
    printf("First Buffer: %s", buf);

    // Display the contents of the second buffer
    printf("Second Buffer: %s", buf1);

    return 0;
}
