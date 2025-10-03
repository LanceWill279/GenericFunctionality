#include <stdio.h>
#include <string.h>

int main() {
    char command[20];  // to hold string like "fwd"
    int value;         // to hold integer like 20

    // Print available options
    printf("Command options:\n");
    printf("fwd <value>   - Move forward\n");
    printf("back <value>  - Move backward\n");
    printf("stop          - Stop motors\n\n");

    // Get user input
    printf("Enter command: ");
    scanf("%s %d", command, &value);  // read string + int

    // Respond based on input
    if (strcmp(command, "fwd") == 0) {
        printf("Set motors to forward %d%%\n", value);
    } else if (strcmp(command, "back") == 0) {
        printf("Set motors to backward %d%%\n", value);
    } else if (strcmp(command, "left") == 0) {
        printf("Set motors to turn left %d%%\n", value);
    } else if (strcmp(command, "right") == 0) {
        printf("Set motors to turn right %d%%\n", value);
    } else if (strcmp(command, "stop") == 0) {
        printf("Motors stopped\n");
    } else {
        printf("Unknown command: %s\n", command);
    }

    return 0;
}
