#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    const char* filename = "important_config";
    const char* content = "important_config";

    int fd = open(filename, O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

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