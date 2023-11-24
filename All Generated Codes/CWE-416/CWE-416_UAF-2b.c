#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <zlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    const char *input_filename = argv[1];
    const char *output_filename = argv[2];

    // Open the input file for reading
    FILE *input_file = fopen(input_filename, "rb");
    if (input_file == NULL) {
        perror("Error opening input file");
        return 1;
    }

    // Read the contents of the file into a buffer
    fseek(input_file, 0, SEEK_END);
    long file_size = ftell(input_file);
    rewind(input_file);

    if (file_size == 0) {
        fclose(input_file);
        printf("File is empty.\n");

        // Save 0 bytes and checksum to the output file
        FILE *output_file = fopen(output_filename, "wb");
        if (output_file == NULL) {
            perror("Error opening output file");
            return 1;
        }

        uint32_t checksum = 0;
        fwrite(&file_size, sizeof(long), 1, output_file);
        fwrite(&checksum, sizeof(uint32_t), 1, output_file);

        fclose(output_file);
        return 0;
    }

    char *buffer = (char *)malloc(file_size);
    if (buffer == NULL) {
        perror("Error allocating memory for buffer");
        fclose(input_file);
        return 1;
    }

    fread(buffer, 1, file_size, input_file);
    fclose(input_file);

    // Calculate the checksum (using CRC32)
    uint32_t checksum = crc32(0L, (const Bytef *)buffer, (uInt)file_size);

    // Save the number of bytes read and the checksum to the output file
    FILE *output_file = fopen(output_filename, "wb");
    if (output_file == NULL) {
        perror("Error opening output file");
        free(buffer);
        return 1;
    }

    fwrite(&file_size, sizeof(long), 1, output_file);
    fwrite(&checksum, sizeof(uint32_t), 1, output_file);

    fclose(output_file);
    free(buffer);

    return 0;
}