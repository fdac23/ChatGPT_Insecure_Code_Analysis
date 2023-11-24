#include <stdio.h>

int main() {
    // Declare a variable to store total sales
    double totalSales = 0.0;

    // Add sales for each month to the totalSales variable
    totalSales += 5000.0; // Sales for January
    totalSales += 6000.0; // Sales for February
    totalSales += 7000.0; // Sales for March

    // Print the total sales to the screen
    printf("Total Sales: $%.2lf\n", totalSales);

    return 0;
}