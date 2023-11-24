#include <stdio.h>
#include <stdlib.h>

// Define a person structure
struct Person {
    char name[50];
    int age;
    int status;
};

// Function to allocate and initialize a person
struct Person *createPerson(const char *name, int age) {
    struct Person *newPerson = (struct Person *)malloc(sizeof(struct Person));
    
    if (newPerson != NULL) {
        strncpy(newPerson->name, name, sizeof(newPerson->name) - 1);
        newPerson->name[sizeof(newPerson->name) - 1] = '\0'; // Ensure null-terminated string
        newPerson->age = age;
        newPerson->status = 0; // Set the status to 0
    }
    
    return newPerson;
}

int main() {
    // Create a new person and initialize it
    struct Person *person = createPerson("John Doe", 30);

    if (person != NULL) {
        printf("Name: %s\n", person->name);
        printf("Age: %d\n", person->age);
        printf("Status: %d\n", person->status);

        // Don't forget to free the allocated memory
        free(person);
    } else {
        printf("Memory allocation failed.\n");
    }

    return 0;
}
