#include "custom_module.h" // Include the custom module with the print function
#include <stdio.h>          // Include the standard library for other functions

int main() {
    // Call the custom print function from the included module
    print("Hello, World!");

    // Use a standard library function to print as well
    printf("This is a standard library function.\n");

    return 0; // Exit the program
}
