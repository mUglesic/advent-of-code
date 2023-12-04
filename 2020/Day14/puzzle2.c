#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include "../fileReader.h"
#include "../stringManipulator.h"
#include "../list.h"

#define LEN_MASK 36

char *toBinary(long n) {
    char *bin = malloc((LEN_MASK + 1) * sizeof(char));

    for (int i = LEN_MASK - 1; i >= 0; i--) {
        
        int index = LEN_MASK - i - 1;

        long curBitValue = pow(2, i);

        if (n >= curBitValue) {
            bin[index] = '1';
            n -= curBitValue;
        }
        else {
            bin[index] = '0';
        }

    }

    bin[LEN_MASK] = '\0';

    return bin;
}

long toDecimal(char *bin) {
    long n = 0;

    for (int i = 0; i < LEN_MASK; i++) {

        int exponent = LEN_MASK - i - 1;

        if (bin[i] == '1') {
            long curBitValue = pow(2, exponent);
            n += curBitValue;
        }


    }

    return n;
}

int parseAddress(char *line) {

    int start = findChar(line, '[');

    char *temp = copyFrom(line, start);

    char *temp2 = copyTo(temp, strlen(temp) - 1);

    int address = atoi(temp2);

    free(temp);
    free(temp2);

    return address;
}

char *parseMask(char **splitMask) {

    char *mask = malloc((LEN_MASK + 1) * sizeof(char));

    strcpy(mask, splitMask[2]);

    return mask;
}

void applyMask(char *value, char *mask) {

    for (int i = 0; i < LEN_MASK; i++) {
        value[i] = (mask[i] != '0') ? mask[i] : value[i];
    }

}

long sumAll(struct List *mem) {
    int n = mem->size;
    long sum = 0;

    for (int i = 0; i < n; i++) {
        sum += listGetByIndex(mem, i)->next->el->value;
    }

    return sum;
}

void writeValues(struct List *mem, char *bin, long value, int index) {
    if (index >= LEN_MASK) {
        // ADD TO LIST
        long address = toDecimal(bin);

        // printf("writing to address: %ld\n", address);

        long index = listGetIndex(mem, createElement(address, 0));

        if (index == -1) {
            listAdd(mem, createElement(address, value));
        }
        else {
            listGetByIndex(mem, index)->next->el->value = value;
        }

        return;
    }

    if (bin[index] == 'X') {

        // printf("index: %d\n", index);

        char *temp = malloc((LEN_MASK + 1) * sizeof(char));

        strcpy(temp, bin);

        temp[index] = '0';

        writeValues(mem, temp, value, index + 1);

        temp[index] = '1';

        writeValues(mem, temp, value, index + 1);

        free(temp);

    }
    else {
        writeValues(mem, bin, value, index + 1);
    }
}

long runProgram(char **program, int n, struct List *mem) {

    char *mask = malloc((LEN_MASK + 1) * sizeof(char));

    for (int i = 0; i < n; i++) {

        char **splitLine = split(program[i], ' ');

        if (strcmp(splitLine[0], "mask") == 0) {
            free(mask);
            mask = parseMask(splitLine);
            printf("\n%s\nNew mask: %s\n\n%s", SEP, mask, SEP);
        }
        else {
            long address = parseAddress(splitLine[0]);
            long value = atol(splitLine[2]);

            char *bin = toBinary(address);

            //printf("\nAddress: %s  (Decimal %ld)\nMask:    %s\n", bin, toDecimal(bin), mask);

            applyMask(bin, mask);

            // mem[address] = toDecimal(bin);

            //printf("Result:  %s\n", bin);

            writeValues(mem, bin, value, 0);

            // printf("wrote values\n");

            free(bin);
        }

        cleanMem(splitLine, 3);

    }

    return sumAll(mem);
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    // long *mem = calloc(USHRT_MAX, sizeof(long));

    struct List mem = createList();

    long sum = runProgram(arr, n, &mem);

    printf("\n%s", SEP);

    printf("\nMEMORY: \n\n");

    listPrintAll(&mem);

    printf("\n%s", SEP);

    printf("Sum of memory: %ld\n", sum);

    printf("%s\n", SEP);

    cleanMem(arr, MAX_LINES);

    return 0;
}