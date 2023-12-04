#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define INSTRUCTION_LENGTH 3

int acc;

struct Instruction {
    char*   type;
    int     arg;
    int     ran;
};

struct Instruction createInstruction(char *type, int arg) {
    struct Instruction ins;
    ins.type = type;
    ins.arg = arg;
    ins.ran = 0;
    return ins;
}

void resetInstructions(struct Instruction *ins, int n) {
    for (int i = 0; i < n; i++) {
        ins[i].ran = 0;
    }
}

void cleanInstructions(struct Instruction *ins, int n) {
    for (int i = 0; i < n; i++) {
        free(ins[i].type);
    }
    free(ins);
}

int getOp(char *type) {
    if (strcmp(type, "acc") == 0) {
        return 1;
    }
    else if (strcmp(type, "jmp") == 0) {
        return 2;
    }
    else if (strcmp(type, "nop") == 0) {
        return 3;
    }
}

int runProgram(struct Instruction *ins, int n) {

    int index = 0;
    acc = 0;

    while (1) {

        if (index < n) printf("\nInstruction \e[1;34m'%s %d'\e[0m (index: %d) has%s been run before!\n", ins[index].type, ins[index].arg, index, ins[index].ran ? "" : " not");

        if (ins[index].ran) {
            printf("\n\e[0;31mExiting program...\e[0m\n\n%s", SEP);
            return -1;
            break;
        }
        else if (index == n) {
            printf("\n\e[0;32mSuccessfully executed program!\e[0m\n\n%s", SEP);
            break;
        }

        int jumped = 0;

        printf("Running instruction %s with argument %d...\n", ins[index].type, ins[index].arg);

        switch (getOp(ins[index].type)) {
            case 1:
                acc += ins[index].arg;
                ins[index].ran = 1;
                break;
            case 2:
                ins[index].ran = 1;
                index += ins[index].arg;
                jumped = 1;
                break;
            case 3:
            default:
                ins[index].ran = 1;
                break;
        }

        if (!jumped) {
            index++;
        }

        printf("\n");

    }

    return 0;
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    struct Instruction *instructions = malloc(n * sizeof(struct Instruction));

    for (int i = 0; i < n; i++) {

        char **tokens = split(arr[i], ' ');

        char *type = malloc((INSTRUCTION_LENGTH + 1) * sizeof(char));
        strcpy(type, tokens[0]);

        int arg = atoi(tokens[1]);

        instructions[i] = createInstruction(type, arg);

        cleanMem(tokens, 2);

    }

    printf(SEP);

    // int returnValue = runProgram(instructions, n);

    for (int i = 0; i < n; i++) {

        char *op = malloc((INSTRUCTION_LENGTH + 1) * sizeof(char));

        strcpy(op, instructions[i].type);

        int returnValue = -1;

        switch (getOp(op)) {
            case 2:
                // JMP -> NOP
                strcpy(instructions[i].type, "nop");
                returnValue = runProgram(instructions, n);
                break;
            case 3:
                // NOP -> JMP
                strcpy(instructions[i].type, "jmp");
                returnValue = runProgram(instructions, n);
                break;
            default:
                break;
        }

        strcpy(instructions[i].type, op);

        free(op);

        if (returnValue == 0) {
            break;
        }

        resetInstructions(instructions, n);

    }

    printf("Value of accumulator: \e[1;34m%d\e[0m\n", acc);

    printf("%s\n", SEP);

    cleanMem(arr, MAX_LINES);
    cleanInstructions(instructions, n);

    return 0;
}