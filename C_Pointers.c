#include <stdio.h>
#include <string.h>

int main() {
    char command[20];  // to hold string like "fwd", just a command string, may be different in STM due to ARM
    int value;         // to hold integer like 20, will be treated as %
    int *ptr;          // pointer to value, with a type of Int, needs to match the datatype of value

    // Print available options
    printf("Command options:\n");
    printf("fwd <value>   - Move forward\n");
    printf("back <value>  - Move backward\n");
    printf("stop          - Stop motors\n\n");

    // Get user input
    printf("Enter command: ");
    scanf("%s %d", command, &value);  
    //Scans both string and digits, to match the desired format

    // assign pointer to the address of value
    ptr = &value;

    // Respond based on input
    // %d%% = %d & %%, so digits with immediate decimal
    //srtcmp is from string library, to compare components of strings
    // Resulting 0 means no comparisons, idk how you are doing this in your code
    if (strcmp(command, "fwd") == 0) {
        printf("Set motors to forward %d%% (via pointer)\n", *ptr);
    } else if (strcmp(command, "back") == 0) {
        printf("Set motors to backward %d%% (via pointer)\n", *ptr);
    } else if (strcmp(command, "stop") == 0) {
        printf("Motors stopped\n");
    } else {
        printf("Unknown command: %s\n", command);
    }

    //Above uses a static address for the value (&value), input changes value directly, with a constant remaining pointer to the static address
    return 0;
}
