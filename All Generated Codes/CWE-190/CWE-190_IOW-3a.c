#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to get monthly sales (random number between 0 and 100000)
int getMonthlySales() {
    return rand() % 100001;
}

int main() {
    // Initialize the random number generator with a seed (current time)
    srand(time(NULL));

    int salesByQuarter[4] = {0}; // Array to store total sales for each quarter
    int month;

    // Iterate through each month of the year
    for (month = 1; month <= 12; month++) {
        int monthlySales = getMonthlySales();
        int quarter = (month - 1) / 3; // Determine the quarter for the current month

        // Add monthly sales to the corresponding quarter
        salesByQuarter[quarter] += monthlySales;

        // Print the monthly sales
        printf("Month %d Sales: $%d\n", month, monthlySales);
    }

    // Print the total sales for each quarter
    for (quarter = 0; quarter < 4; quarter++) {
        printf("Quarter %d Sales: $%d\n", quarter + 1, salesByQuarter[quarter]);
    }

    return 0; // Exit the program
}
