#include <stdio.h>
#include <stdlib.h>

int main() {
    char buf[1024]; // Allocate a buffer of 1024 bytes

    printf("Enter up to 10 characters: ");
    
    // Use fgets to read up to 10 characters from standard input
    if (fgets(buf, sizeof(buf), stdin) != NULL) {
        // Ensure that the input is null-terminated
        buf[10] = '\0';

        // Print the content of the buffer
        printf("You entered: %s\n", buf);
    } else {
        printf("Error reading input\n");
    }

    return 0;
}