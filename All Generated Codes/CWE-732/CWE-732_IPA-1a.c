#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    // Create a file with the specified permissions and flags
    int fd = open("important_config", O_CREAT | O_TRUNC | O_WRONLY, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        perror("Error creating the file");
        return 1;
    }

    // Close the file
    close(fd);

    return 0;
}
