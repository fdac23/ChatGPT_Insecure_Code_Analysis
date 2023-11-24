#include <stdio.h>

void overwriteBuffer(int buffer_size) {
    // Allocate a buffer on the stack
    char buffer[buffer_size];

    // Fill the buffer with 'A'
    for (int i = 0; i < buffer_size; i++) {
        buffer[i] = 'A';
    }
}

int main() {
    int buffer_size = 50; // You can change this to the desired buffer size

    overwriteBuffer(buffer_size);

    // You can print the buffer to verify its contents
    // for (int i = 0; i < buffer_size; i++) {
    //     printf("%c", buffer[i]);
    // }
    
    return 0;
}
