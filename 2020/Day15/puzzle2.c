#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define N 30000000

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);

    char **starting = split(arr[0], ',');
    int nStarting = countChars(arr[0], ',') + 1;

    int *spoken = malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        spoken[i] = -1;
    }

    int prev = 0;

    for (int i = 0; i < nStarting; i++) {
        spoken[atoi(starting[i])] = i;
        prev = atoi(starting[i]);
    }

    for (int i = nStarting; i < N; i++) {
        
        int prevIndex = spoken[prev];

        if (prevIndex == -1 || i == nStarting) {
            int zeroIndex = spoken[0];
            if (zeroIndex == -1) {
                spoken[0] = i;
            }
            prev = 0;
        }
        else {
            int nextNum = i - 1 - spoken[prev];
            if (spoken[nextNum] == -1) {
                spoken[nextNum] = i;
            }
            spoken[prev] = i - 1;
            prev = nextNum;
        }

    }

    printf("%dth number: %d\n", N, prev);

    free(spoken);
    cleanMem(starting, nStarting);
    cleanMem(arr, MAX_LINES);

    return 0;
}