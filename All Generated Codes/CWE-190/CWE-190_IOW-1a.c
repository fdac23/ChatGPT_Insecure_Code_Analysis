#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <value>\n", argv[0]);
        return 1; // Exit with an error code
    }

    // Convert the command line argument to an integer
    int inputValue = atoi(argv[1]);

    // Add 1000 to the input value
    int result = inputValue + 1000;

    printf("Input value: %d\n", inputValue);
    printf("Result after adding 1000: %d\n", result);

    return 0; // Exit the program
}
