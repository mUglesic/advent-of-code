#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

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
        value[i] = (mask[i] != 'X') ? mask[i] : value[i];
    }

}

long sumArray(long *arr, int n) {
    long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

long runProgram(char **program, int n, long *mem) {

    char *mask = malloc((LEN_MASK + 1) * sizeof(char));

    for (int i = 0; i < n; i++) {

        char **splitLine = split(program[i], ' ');

        if (strcmp(splitLine[0], "mask") == 0) {
            free(mask);
            mask = parseMask(splitLine);
            printf("\n%s\nNew mask: %s\n\n%s", SEP, mask, SEP);
        }
        else {
            int address = parseAddress(splitLine[0]);
            long value = atol(splitLine[2]);

            char *bin = toBinary(value);

            printf("\nValue:  %s  (Decimal %ld)\nMask:   %s\n", bin, value, mask);

            applyMask(bin, mask);

            mem[address] = toDecimal(bin);

            printf("Result: %s  (Decimal %ld)\n", bin, mem[address]);

            free(bin);
        }

        cleanMem(splitLine, 3);

    }

    return sumArray(mem, USHRT_MAX);
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    long *mem = calloc(USHRT_MAX, sizeof(long));

    long sum = runProgram(arr, n, mem);

    printf("\n%s", SEP);

    printf("Sum of memory: %ld\n", sum);

    printf("%s\n", SEP);

    free(mem);
    cleanMem(arr, MAX_LINES);

    return 0;
}