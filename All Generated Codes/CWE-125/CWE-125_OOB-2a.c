#include <stdio.h>

// Array of integers
int id_sequence[] = {10, 20, 30, 40, 50};

int getValueAtIndex(int index) {
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);

    if (index < 0 || index >= size) {
        return -1; // Index out of bounds, return -1
    }

    return id_sequence[index];
}

int main() {
    int userIndex;

    printf("Enter an index: ");
    if (scanf("%d", &userIndex) != 1) {
        printf("Invalid input. Please enter an integer.\n");
        return 1; // Exit with an error code
    }

    int result = getValueAtIndex(userIndex);

    if (result == -1) {
        printf("Index out of bounds. Returning -1.\n");
    } else {
        printf("Value at index %d: %d\n", userIndex, result);
    }

    return 0; // Exit the program
}
