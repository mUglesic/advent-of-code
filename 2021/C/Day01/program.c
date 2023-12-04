#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../buglLib/fileReader.h"
// #include "../buglLib/stringManipulator.h"

#define MAX_STR_LEN 5

int solve1(char** arr, int n) {

    int counter = 0;

    for (int i = 0; i < n - 1; i++) {

        int current = atoi(arr[i]);
        int next = atoi(arr[i + 1]);

        if (next > current) {
            counter++;
        }

    }

    return counter;

}

int solve2(char** arr, int n) {

    int len = n - 2;
    char** newArr = create2DcharArray(len, MAX_STR_LEN);

    for (int i = 0; i < len; i++) {

        sprintf(newArr[i], "%d", (atoi(arr[i]) + atoi(arr[i + 1]) + atoi(arr[i + 2])));

    }

    return solve1(newArr, len);

}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);
    int n = arrlen(arr);

    int res1 = solve1(arr, n);
    int res2 = solve2(arr, n);

    printf("Part One: %d\n", res1);
    printf("Part Two: %d\n", res2);

    cleanMem(arr, MAX_LINES);

    return 0;

}