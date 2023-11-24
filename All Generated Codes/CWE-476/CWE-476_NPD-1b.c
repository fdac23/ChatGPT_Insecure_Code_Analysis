#include <stdio.h>
#include <stdlib.h>

// Define a person struct
struct person {
    char name[50];
    int age;
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

    // You can access and modify other fields of the struct as well
    // Example:
    // strcpy(p->name, "John");
    // p->age = 30;

    // Don't forget to free the allocated memory when done
    free(p);

    return 0;
}