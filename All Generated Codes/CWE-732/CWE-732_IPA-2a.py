#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    // Open the file for reading and writing, creating it if it doesn't exist
    int fd = open("important_config", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);

    if (fd == -1) {
        perror("Error opening the file");
        return 1;
    }

    // String to write to the file
    const char *content = "important_config";

    // Write the string to the file
    ssize_t bytes_written = write(fd, content, strlen(content));

    if (bytes_written == -1) {
        perror("Error writing to the file");
        close(fd);
        return 1;
    }

    // Close the file
    close(fd);

    return 0;
}
