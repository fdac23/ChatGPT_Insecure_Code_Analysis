#include <stdio.h>

// Function to retrieve a value at a specified index in id_sequence
int getValueAtIndex(int index, int id_sequence[], int size) {
    if (index >= 0 && index < size) {
        return id_sequence[index];
    } else {
        return 0;
    }
}

int main() {
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);
    int index;

    // Prompt the user for an index value
    printf("Enter an index value: ");
    scanf("%d", &index);

    // Call the function to get the value at the specified index
    int result = getValueAtIndex(index, id_sequence, size);

    // Print the result
    if (result != 0) {
        printf("Value at index %d: %d\n", index, result);
    } else {
        printf("Index out of bounds or invalid.\n");
    }

    return 0;
}