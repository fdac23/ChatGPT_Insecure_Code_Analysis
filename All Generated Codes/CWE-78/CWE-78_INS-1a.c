#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *username = "your_username"; // Replace with the desired username

    // Using system() function to execute the command
    printf("Using system() function:\n");
    char system_cmd[100];
    snprintf(system_cmd, sizeof(system_cmd), "getent passwd %s", username);
    int sys_result = system(system_cmd);
    if (sys_result != 0) {
        fprintf(stderr, "Error executing the system command.\n");
    }

    // Using popen() function to execute the command
    printf("\nUsing popen() function:\n");
    char popen_cmd[100];
    snprintf(popen_cmd, sizeof(popen_cmd), "getent passwd %s", username);
    FILE *output = popen(popen_cmd, "r");
    if (output == NULL) {
        fprintf(stderr, "Error executing the popen command.\n");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), output) != NULL) {
        printf("%s", line);
    }

    pclose(output);

    return 0;
}
