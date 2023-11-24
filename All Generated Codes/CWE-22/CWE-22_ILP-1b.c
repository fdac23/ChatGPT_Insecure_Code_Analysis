#include <stdio.h>
#include <string.h>

int main() {
    char filename[100];
    char path[150] = "/safe/";

    printf("Enter the filename to read (e.g., file.txt): ");
    if (scanf("%s", filename) == 1) {
        // Concatenate the filename with the path to form the complete file path
        strcat(path, filename);

        FILE *file = fopen(path, "r");
        if (file != NULL) {
            char buffer[1024];
            while (fgets(buffer, sizeof(buffer), file)) {
                printf("%s", buffer);
            }
            fclose(file);
        } else {
            printf("Failed to open the file.\n");
        }
    } else {
        printf("Invalid input.\n");
    }

    return 0;
}