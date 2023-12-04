#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../../fileReader.h"

void printArray(int *arr, int n) {
	printf("[");
	for (int i = 0; i < n; i++) {
		printf("%d%s", arr[i], (i == n - 1) ? "" : ", ");
	}
	printf("]\n");
}

int countChars(char* s, char c) {
    int counter = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == c) {
            counter++;
        }
    }
    return counter;
}

int* parseProgram(char* program, int n) {
    int* newProgram = calloc(n, sizeof(int));
    char* buff = calloc(255, sizeof(char));
    int curIndex = 0;
    char curChar;

    for (int i = 0; i < n; i++) {

        while((curChar = program[curIndex]) != ',' && curIndex < strlen(program)) {

            strncat(buff, &curChar, 1);

            curIndex++;

        }

        newProgram[i] = atoi(buff);

        buff = calloc(255, sizeof(char));
        curIndex++;

    }

    free(buff);

    return newProgram;
}

int doOp(int* tokens, int token, int i) {
    int plusOne, plusTwo, plusThree;
    // printf("opcode: %d\n", token);
    switch(token) {
        case 1:
            plusOne = tokens[i + 1];
            plusTwo = tokens[i + 2];
            plusThree = tokens[i + 3];
            tokens[plusThree] = tokens[plusOne] + tokens[plusTwo];
            break;
        case 2:
            plusOne = tokens[i + 1];
            plusTwo = tokens[i + 2];
            plusThree = tokens[i + 3];
            tokens[plusThree] = tokens[plusOne] * tokens[plusTwo];
            break;
        case 99:
            return -1;
        default:
            return -1;
    }
    return 0;
}

void restoreProgram(int* tokens, int a, int b) {
    tokens[1] = a;
    tokens[2] = b;
}

int* runProgram(char* program, int target) {
    int n = countChars(program, ',') + 1;
    int* tokens = parseProgram(program, n);

    for (int a = 0; a <= 99; a++) {
        for (int b = 0; b <= 99; b++) {
            restoreProgram(tokens, a, b);
            for (int i = 0; i < n; i += 4) {
                if (doOp(tokens, tokens[i], i) == -1) break;
            }
            if (tokens[0] == target) {
                printf("noun: %d, verb:%d, result: %d\n", a, b, ((100 * a) + b));
                return tokens;
            }
            tokens = parseProgram(program, n);
        }
    }

    return tokens;
}

int main(int argc, char** argv) {

    char** programs = readFile(argv[1]);

    int* final = runProgram(programs[0], 19690720);

    // printArray(final, countChars(programs[0], ',') + 1);

    printf("Value at index 0: %d\n", final[0]);

    free(final);
    cleanMem(programs, MAX_LINES);

    return 0;
}