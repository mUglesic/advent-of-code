#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../buglLib/fileReader.h"
#include "../buglLib/stringManipulator.h"

int solve1(char** arr, int n) {

    int pos = 0;
    int depth = 0;

    for (int i = 0; i < n; i++) {

        char** command = split(arr[i], ' ');

        if (strcmp(command[0], "forward") == 0) {

            pos += atoi(command[1]);

        }
        else if (strcmp(command[0], "down") == 0) {

            depth += atoi(command[1]);

        }
        else if (strcmp(command[0], "up") == 0) {

            depth -= atoi(command[1]);

        }

        cleanMem(command, 2);

    }

    printf("Part One | Position: %d | Depth: %d\n", pos, depth);

    return (pos * depth);

}

int solve2(char** arr, int n) {

    int pos = 0;
    int depth = 0;
    int aim = 0;

    for (int i = 0; i < n; i++) {

        char** command = split(arr[i], ' ');

        if (strcmp(command[0], "forward") == 0) {

            pos += atoi(command[1]);
            depth += (aim * atoi(command[1]));

        }
        else if (strcmp(command[0], "down") == 0) {

            aim += atoi(command[1]);

        }
        else if (strcmp(command[0], "up") == 0) {

            aim -= atoi(command[1]);

        }

        cleanMem(command, 2);

    }

    printf("Part Two | Position: %d | Depth: %d\n", pos, depth);

    return (pos * depth);

}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);
    int n = arrlen(arr);

    int res1 = solve1(arr, n);
    printf("Result: %d\n", res1);
    
    int res2 = solve2(arr, n);
    printf("Result: %d\n", res2);

    cleanMem(arr, MAX_LINES);

    return 0;

}