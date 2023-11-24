#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the maximum username length
#define MAX_USERNAME_LENGTH 100

// Function to generate a hello message
void generateHelloResponse(const char *username, char *response, size_t responseSize) {
    snprintf(response, responseSize, "Hello %s", username);
}

// Function to handle the HTTP hello page request
void http_hello_page(FILE *request, FILE *response) {
    char username[MAX_USERNAME_LENGTH];
    char responseBuffer[256];  // Adjust the buffer size as needed

    // Read the username from the request
    if (fgets(username, MAX_USERNAME_LENGTH, request) == NULL) {
        // Handle error reading username
        fprintf(response, "Error: Unable to read the username from the request.");
        return;
    }

    // Remove trailing newline character, if present
    size_t usernameLength = strlen(username);
    if (usernameLength > 0 && username[usernameLength - 1] == '\n') {
        username[usernameLength - 1] = '\0';
    }

    // Generate the response
    generateHelloResponse(username, responseBuffer, sizeof(responseBuffer));

    // Write the response to the response file stream
    fprintf(response, "HTTP/1.1 200 OK\r\n");
    fprintf(response, "Content-Type: text/plain\r\n");
    fprintf(response, "\r\n"); // End of headers
    fprintf(response, "%s", responseBuffer);
}

int main() {
    // Example usage: Open request and response file streams
    FILE *request = fopen("request.txt", "r");
    FILE *response = fopen("response.txt", "w");

    if (request == NULL || response == NULL) {
        perror("fopen");
        return 1;
    }

    // Call the http_hello_page function
    http_hello_page(request, response);

    // Close the file streams
    fclose(request);
    fclose(response);

    return 0;
}