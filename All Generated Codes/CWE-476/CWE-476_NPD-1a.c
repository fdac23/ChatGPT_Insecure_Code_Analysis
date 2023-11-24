#include <stdio.h>
#include <stdlib.h>

// Define a person structure
struct Person {
    char name[50];
    int age;
};

int main() {
    // Declare a pointer to a person
    struct Person *person_ptr;

    // Allocate memory for a person structure
    person_ptr = (struct Person*)malloc(sizeof(struct Person));

    // Check if memory allocation was successful
    if (person_ptr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Populate the structure using the pointer and -> operator
    printf("Enter name: ");
    scanf("%s", person_ptr->name);  // Use -> to access struct members

    printf("Enter age: ");
    scanf("%d", &person_ptr->age);

    // Display the entered information
    printf("Name: %s\n", person_ptr->name);
    printf("Age: %d\n", person_ptr->age);

    // Free the allocated memory
    free(person_ptr);

    return 0;
}
