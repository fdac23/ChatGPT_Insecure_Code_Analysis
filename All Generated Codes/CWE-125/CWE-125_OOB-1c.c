#include <stdio.h>
#include <stdlib.h>

int getValueFromArray(const int array[], int size, int index) {
    if (index >= 0 && index < size) {
        return array[index];
    } else {
        return -1;
    }
}

int main() {
    // Define an array of integers
    int id_sequence[] = {10, 20, 30, 40, 50};
    int array_size = sizeof(id_sequence) / sizeof(id_sequence[0]);

    // Read an integer from the standard input
    int input_index;
    printf("Enter an index: ");
    if (scanf("%d", &input_index) != 1) {
        fprintf(stderr, "Invalid input. Please enter an integer.\n");
        return 1;  // Exit with an error code
    }

    // Call getValueFromArray and use the return value as the exit code
    int result = getValueFromArray(id_sequence, array_size, input_index);
    return result;
}