#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <zlib.h>

#define BUFFER_SIZE 1024  // Adjust this to your desired buffer size

// Function to calculate the CRC32 checksum of a buffer
uint32_t calculateChecksum(const void *data, size_t size) {
    uint32_t checksum = crc32(0L, Z_NULL, 0);
    checksum = crc32(checksum, data, size);
    return checksum;
}

int main() {
    FILE *inputFile, *outputFile;
    char inputFileName[] = "input.txt";   // Change to your input file name
    char outputFileName[] = "output.txt"; // Change to your output file name

    // Open the input file for reading
    inputFile = fopen(inputFileName, "rb");
    if (inputFile == NULL) {
        perror("Error opening input file");
        return 1;
    }

    // Read the contents of the file into a buffer
    char buffer[BUFFER_SIZE];
    size_t bytesRead = fread(buffer, 1, BUFFER_SIZE, inputFile);

    // Calculate the CRC32 checksum of the buffer
    uint32_t checksum = calculateChecksum(buffer, bytesRead);

    // Open the output file for writing the results
    outputFile = fopen(outputFileName, "w");
    if (outputFile == NULL) {
        perror("Error opening output file");
        fclose(inputFile);
        return 1;
    }

    // Write the number of bytes read and the checksum to the output file
    fprintf(outputFile, "Bytes Read: %lu\n", bytesRead);
    fprintf(outputFile, "Checksum: %u\n", checksum);

    // Close the files
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
