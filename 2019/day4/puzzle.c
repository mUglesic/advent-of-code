#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../fileReader.h"
#include "../../stringManipulator.h"

int isSixDigit(int n) {
    char* ns = malloc(7 * sizeof(char));
    sprintf(ns, "%d", n);
    return strlen(ns) == 6;
}

int isWithinRange(int n, int start, int end) {
    return n >= start && n <= end;
}

int hasEqualAdjacentDigits(int n) {
    char* ns = malloc(7 * sizeof(char));
    sprintf(ns, "%d", n);
    char prev = ns[0];
    char cur;
    int sameCounter = 1;
    for (int i = 1; i < strlen(ns); i++) {
        cur = ns[i];
        if (prev == cur) {
            sameCounter++;
        }
        else {
            if (sameCounter == 2) {
                return 1;
            }
            sameCounter = 1;
        }
        prev = cur;
    }
    free(ns);
    return sameCounter == 2;
}

int neverDecreases(int n) {
    char* ns = malloc(7 * sizeof(char));
    sprintf(ns, "%d", n);
    char prev = ns[0];
    char cur;
    for (int i = 1; i < strlen(ns); i++) {
        cur = ns[i];
        if (prev > cur) return 0;
        prev = cur;
    }
    return 1;
}

int checkCriteria(int n, int start, int end) {
    return isSixDigit(n) && isWithinRange(n, start, end) && hasEqualAdjacentDigits(n) && neverDecreases(n);
}

int countPasswords(char** range) {
    
    int start = atoi(range[0]);
    int end = atoi(range[1]);

    int counter = 0;

    for (int i = start; i < end; i++) {
        counter += checkCriteria(i, start, end);
    }

    return counter;
}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);

    char** range = split(arr[0], '-');

    printf("%s -> %s\n", range[0], range[1]);

    int n = countPasswords(range);

    printf("Possible passwords: %d\n", n);

    cleanMem(range, 2);
    cleanMem(arr, MAX_LINES);

    return 0;
}