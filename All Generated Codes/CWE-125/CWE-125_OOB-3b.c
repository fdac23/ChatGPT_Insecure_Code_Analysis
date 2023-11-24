#include <stdio.h>

// Define the array
int id_sequence[] = {10, 20, 30, 40, 50};
int array_size = sizeof(id_sequence) / sizeof(id_sequence[0]);

// Function to get a value from the array by index
int getValueAtIndex(int index) {
    if (index >= 0 && index < array_size) {
        return id_sequence[index];
    } else {
        return -1;
    }
}

int main() {
    int index;

    // Prompt the user for an index
    printf("Enter an index: ");
    if (scanf("%d", &index) == 1) {
        int result = getValueAtIndex(index);

        if (result == -1) {
            printf("Index is out of bounds.\n");
        } else {
            printf("Value at index %d is: %d\n", index, result);
        }
    } else {
        printf("Invalid input. Please enter a valid integer index.\n");
    }

    return 0;
}