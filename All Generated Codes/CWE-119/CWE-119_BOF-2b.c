#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <integer>\n", argv[0]);
        return 1;
    }

    // Convert the command-line argument to an integer
    int inputInt = atoi(argv[1]);

    // Define an array and its range
    int array[] = {10, 20, 30, 40, 50};
    int arraySize = sizeof(array) / sizeof(array[0]);

    if (inputInt >= 0 && inputInt < arraySize) {
        // Check if the input integer is within the array range
        int element = array[inputInt];
        printf("Element at index %d is: %d\n", inputInt, element);
    } else {
        printf("Invalid input. Input integer is not within the array range.\n");
    }

    return 0;
}