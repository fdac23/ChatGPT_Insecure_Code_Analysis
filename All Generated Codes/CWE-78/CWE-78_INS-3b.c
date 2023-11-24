#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>

// Execute a command
void executeCommand(const char *command) {
    system(command);
}

// A custom print function that works similarly to printf
void customPrint(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
}

int main() {
    const char *command = "ls -l"; // Example command

    // Execute the command
    executeCommand(command);

    // Use the custom print function
    customPrint("This is a custom print function.\n");

    return 0;
}