#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int runIdCommand(const char *username) {
    char command[100];
    int exit_status;

    // Build the command to run "id" with the specified username
    snprintf(command, sizeof(command), "id %s", username);

    // Use the system() function to run the command
    exit_status = system(command);

    return exit_status;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        return 1;
    }

    const char *username = argv[1];

    // Run the "id" command and get the exit status
    int exit_status = runIdCommand(username);

    printf("Exit status of 'id %s': %d\n", username, exit_status);

    return 0;
}