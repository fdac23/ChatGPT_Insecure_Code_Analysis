#include <stdio.h>
#include <stdlib.h>

// Define a struct for a person
struct Person {
    char name[50];
    int age;
    int status;
};

int main() {
    // Allocate memory for a new person
    struct Person *newPerson = (struct Person *)malloc(sizeof(struct Person));

    if (newPerson == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1; // Exit with an error code
    }

    // Set the status of the new person to 0 using the -> operator
    newPerson->status = 0;

    // You can also access other members and set them as needed
    // For example:
    // strcpy(newPerson->name, "John");
    // newPerson->age = 30;

    // Use the person struct
    printf("New person's status: %d\n", newPerson->status);

    // Free the allocated memory when it's no longer needed
    free(newPerson);

    return 0; // Exit with success
}