#include <stdio.h>
#include <stdlib.h>

void executeCommand(const char *command) {
    FILE *fp;
    char buffer[128];

    fp = popen(command, "r");
    if (fp == NULL) {
        perror("popen");
        exit(1);
    }

    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    pclose(fp);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        return 1;
    }

    char username[128];
    snprintf(username, sizeof(username), "cat /etc/passwd | grep %s", argv[1]);

    executeCommand(username);

    return 0;
}