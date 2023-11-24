#include <stdio.h>

// Function to get a value from an array by index
int getValueFromArray(int array[], int size, int index) {
    if (index >= 0 && index < size) {
        return array[index];
    } else {
        return -1;
    }
}

int main() {
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);

    int index;
    printf("Enter an index: ");
    if (scanf("%d", &index) == 1) {
        int result = getValueFromArray(id_sequence, size, index);
        if (result == -1) {
            printf("Index is out of bounds.\n");
            return -1;
        } else {
            printf("Value at index %d is: %d\n", index, result);
            return result;
        }
    } else {
        printf("Invalid input. Please enter a valid integer index.\n");
        return -1;
    }
}