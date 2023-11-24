#include <stdio.h>

int main() {
    const char *filename = "/safe/your_file.txt"; // Replace with the actual file path

    // Open the file for reading
    FILE *file = fopen(filename, "r");

    if (file) {
        // File was opened successfully
        char buffer[1024]; // A buffer to read the file contents

        while (fgets(buffer, sizeof(buffer), file) != NULL) {
            // Process the contents of the file (e.g., print it)
            printf("%s", buffer);
        }

        // Close the file when you're done
        fclose(file);
    } else {
        // File could not be opened
        perror("Error opening file");
        return 1;
    }

    return 0;
}
