#include <stdio.h>

int getValueFromArray(const int *array, int size, int index) {
    if (index < 0 || index >= size) {
        return -1; // Index out of bounds, return -1
    }
    return array[index];
}

int main() {
    int id_sequence[] = {1, 2, 3, 4, 5};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);
    int userIndex;

    printf("Enter an index: ");
    if (scanf("%d", &userIndex) != 1) {
        printf("Invalid input. Please enter an integer.\n");
        return 1; // Exit with an error code
    }

    int result = getValueFromArray(id_sequence, size, userIndex);

    if (result == -1) {
        printf("Index out of bounds. Returning -1.\n");
        return -1; // Exit with an error code
    } else {
        printf("Value at index %d: %d\n", userIndex, result);
        return result; // Exit with the value from the array
    }
}
