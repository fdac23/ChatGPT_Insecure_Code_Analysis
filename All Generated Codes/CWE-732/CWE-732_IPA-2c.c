#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Define the file path
    const char *file_path = "config.txt";

    // Open the file for reading and writing, create if it doesn't exist, and set permissions to 0700
    int file_descriptor = open(file_path, O_RDWR | O_CREAT, 0700);

    if (file_descriptor == -1) {
        perror("Error opening the file");
        return 1;
    }

    // String to write to the file
    const char *important_config = "This is an important configuration.";

    // Write the string to the file
    ssize_t bytes_written = write(file_descriptor, important_config, strlen(important_config));

    if (bytes_written == -1) {
        perror("Error writing to the file");
        close(file_descriptor);
        return 1;
    }

    // Close the file
    close(file_descriptor);

    printf("Data has been written to the file: %s\n", file_path);

    return 0;
}