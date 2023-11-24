#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Initialize the random number generator with the current time
    srand((unsigned)time(NULL));

    // Generate three random integers larger than 1000
    int a = rand() % 9000 + 1001;
    int b = rand() % 9000 + 1001;
    int c = rand() % 9000 + 1001;

    // Calculate the sum of the integers
    int sum = a + b + c;
    long long sum2 = (long long)a + (long long)b + (long long)c;

    // Print the integers and their sums
    printf("a: %d\nb: %d\nc: %d\nsum: %d\nsum2: %lld\n", a, b, c, sum, sum2);

    return 0;
}