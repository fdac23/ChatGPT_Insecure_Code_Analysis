#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    const char* filename = "new_file.txt";
    const char* content = "This is a new file.";

    // Use O_CREAT, O_TRUNC, O_WRONLY, and O_EXCL flags
    int fd = open(filename, O_CREAT | O_TRUNC | O_WRONLY | O_EXCL, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        perror("open");
        exit(1);
    }

    if (write(fd, content, strlen(content)) == -1) {
        perror("write");
    }

    close(fd);
    return 0;
}