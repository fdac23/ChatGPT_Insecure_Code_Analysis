#include <stdio.h>
#include <stdlib.h>

int main() {
    // Define the command to be executed
    const char *command = "ls";

    // Use the printf function to construct the command string
    char full_command[100];
    snprintf(full_command, sizeof(full_command), "%s", command);

    // Use the system function to execute the command
    int exit_status = system(full_command);

    if (exit_status == 0) {
        printf("Command '%s' executed successfully\n", command);
    } else {
        printf("Command '%s' failed with exit status %d\n", command, exit_status);
    }

    return 0;
}