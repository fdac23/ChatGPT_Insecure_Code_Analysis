#include <stdio.h>

// Structure to represent a vehicle
struct Vehicle {
    char make[50];
    char model[50];
    int year;
};

int main() {
    // Array of vehicles
    struct Vehicle vehicles[] = {
        {"Toyota", "Camry", 2022},
        {"Ford", "F-150", 2021},
        {"Honda", "Civic", 2020},
        {"Chevrolet", "Silverado", 2022}
    };

    int numVehicles = sizeof(vehicles) / sizeof(vehicles[0]);

    // Prompt the user to enter an index
    int index;
    printf("Enter an index (0 to %d) to access a vehicle: ", numVehicles - 1);
    scanf("%d", &index);

    // Check if the entered index is valid
    if (index >= 0 && index < numVehicles) {
        // Access and print the vehicle at the specified index
        struct Vehicle selectedVehicle = vehicles[index];
        printf("Vehicle at index %d:\n", index);
        printf("Make: %s\n", selectedVehicle.make);
        printf("Model: %s\n", selectedVehicle.model);
        printf("Year: %d\n", selectedVehicle.year);
    } else {
        printf("Invalid index. Please enter a valid index between 0 and %d.\n", numVehicles - 1);
    }

    return 0;
}
