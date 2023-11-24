#include <stdio.h>

int getValueAtIndex(int input, int id_sequence[], int size) {
    if (input >= 0 && input < size) {
        return id_sequence[input];
    } else {
        return -1;
    }
}

int main() {
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);
    int input;

    // Prompt the user for an input integer
    printf("Enter an integer as an index: ");
    scanf("%d", &input);

    // Call the function to get the value at the specified index
    int result = getValueAtIndex(input, id_sequence, size);

    // Print the result
    if (result != -1) {
        printf("Value at index %d: %d\n", input, result);
    } else {
        printf("Index out of bounds or invalid.\n");
    }

    return 0;
}