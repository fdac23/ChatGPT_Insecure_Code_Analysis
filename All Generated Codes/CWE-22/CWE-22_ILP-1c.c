#include <stdio.h>

int main() {
    FILE *file;
    char filename[] = "safe/directory/file.txt";  // Path to the file in the safe directory
    char buffer[100];  // A buffer to store the file content

    // Open the file for reading
    file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening the file");
        return 1;  // Exit with an error code
    }

    // Read and print the file content
    while (fgets(buffer, sizeof(buffer), file)) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);

    return 0;  // Exit with success
}