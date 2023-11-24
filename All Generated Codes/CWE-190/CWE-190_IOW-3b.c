#include <stdio.h>

// Function to simulate getting monthly sales
int getMonthlySales(int month) {
    // Simulated monthly sales data
    int monthlyData[] = {5000, 6000, 7000};

    // Check if the month value is within a valid range
    if (month >= 0 && month < 3) {
        return monthlyData[month];
    } else {
        // Handle invalid month values (you can return an error code or handle it as needed)
        return -1;
    }
}

int main() {
    int sum = 0;

    // Iterate over 3 months
    for (int i = 0; i < 3; i++) {
        int monthlySales = getMonthlySales(i);

        if (monthlySales != -1) {
            // Add the monthly sales to the sum
            sum += monthlySales;
        } else {
            printf("Invalid month encountered.\n");
            return 1;
        }
    }

    printf("Total sales for the first quarter: %d\n", sum);

    return 0;
}