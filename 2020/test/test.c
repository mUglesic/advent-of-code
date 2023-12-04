#include <stdio.h>
#include <stdlib.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);

    char **splitArr = split(arr[0], ':');
    int nSplitArr = countChars(arr[0], ':') + 1;

    char *limits = copyFrom(splitArr[1], 0);

    printn2DArray(splitArr, nSplitArr);
    printf("%s\n", limits);

    free(limits);
    cleanMem(splitArr, nSplitArr);
    cleanMem(arr, MAX_LINES);

    return 0;
}