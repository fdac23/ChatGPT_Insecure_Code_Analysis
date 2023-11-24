#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a person struct
struct person {
    char name[50];
    int status;
};

int main() {
    // Allocate memory for a person struct
    struct person *p = (struct person *)malloc(sizeof(struct person));

    if (p == NULL) {
        perror("Memory allocation failed");
        return 1;
    }

    // Initialize the status field to 0
    p->status = 0;

    // Set the name field to "John"
    strcpy(p->name, "John");

    // Access and modify other fields of the struct using the -> operator
    // Example:
    // p->age = 30;

    // Don't forget to free the allocated memory when done
    free(p);

    return 0;
}