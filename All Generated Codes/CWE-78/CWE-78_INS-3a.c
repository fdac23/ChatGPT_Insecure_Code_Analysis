#include <stdio.h>
#include <stdlib.h>

int main() {
    // Create a format string with a placeholder for the command
    const char *format = "ls %s";

    // Command to execute (listing the current directory)
    const char *command = ".";

    // Calculate the size of the buffer needed for the command
    size_t cmd_size = snprintf(NULL, 0, format, command) + 1;
    char *full_command = (char *)malloc(cmd_size);

    // Create the full command string
    snprintf(full_command, cmd_size, format, command);

    // Execute the command using the system() function
    int return_code = system(full_command);

    // Check the return code for success or failure
    if (return_code == 0) {
        printf("Command executed successfully.\n");
    } else {
        printf("Command execution failed.\n");
    }

    // Free the allocated memory
    free(full_command);

    return 0;
}
