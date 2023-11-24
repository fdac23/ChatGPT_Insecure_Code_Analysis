#include <stdio.h>

int main() {
    // Array of strings representing vehicles
    char *vehicles[] = {
        "Car",
        "Bicycle",
        "Bus",
        "Motorcycle",
        "Truck"
    };

    // Calculate the number of elements in the array
    int numVehicles = sizeof(vehicles) / sizeof(vehicles[0]);

    // Prompt the user for the index of a vehicle
    int index;
    printf("Enter the index of a vehicle (0 to %d): ", numVehicles - 1);
    scanf("%d", &index);

    // Check if the entered index is within bounds
    if (index >= 0 && index < numVehicles) {
        // Return the selected vehicle
        printf("Selected Vehicle: %s\n", vehicles[index]);
    } else {
        printf("Invalid index. Please enter a valid index.\n");
    }

    // Loop through the array and print each vehicle
    printf("List of Vehicles:\n");
    for (int i = 0; i < numVehicles; i++) {
        printf("%d: %s\n", i, vehicles[i]);
    }

    return 0;
}