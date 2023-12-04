#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"
#include "../sorter.h"

#define BUILT_IN 3

int *charToIntArr(char **arr, int n) {
    int *newArr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {

        newArr[i] = atoi(arr[i]);

    }

    return newArr;
}

int maxFromArr(int *arr, int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        max = max < arr[i] ? arr[i] : max;
    }
    return max;
}

void countJoltages(int *adapters, int n, int *joltages) {

    int prev = adapters[0];

    for (int i = 1; i < n; i++) {

        int change = adapters[i] - prev;

        printf("\nCurrent adapter: %d | Change: [%d]\n", adapters[i], change);

        joltages[change - 1]++;

        prev = adapters[i];

    }

}

long configure(int *adapters, int n, int index, long *memo, int prevAdapter) {

    if (index >= n) {
        return 1;
    }

    if (memo[index] > 0) {
        return memo[index];
    }

    int adapter;
    int i = index;

    long counter = 0;

    while ((adapter = adapters[i]) <= prevAdapter + 3 && i < n) {
        //printf("testing index: %d value: %d\n", i, adapter);
        long temp = configure(adapters, n, i + 1, memo, adapter);
        //printf("memo: %ld | temp: %ld\n", memo[i], temp);
        memo[i] = memo[i] > temp ? memo[i] : temp;
        counter += memo[i];
        i++;
    }

    //printf("counter: %d\n", counter);

    return counter;
}

long countConfigs(int *adapters, int n, long *memo) {

    long counter = 0;

    int adapter;
    int i = 1;

    while ((adapter = adapters[i]) <= 3) {
        printf("\nchecking start index: %d value: %d\n", i, adapter);
        long temp = configure(adapters, n, i + 1, memo, adapter);
        //printf("memo: %ld | temp: %ld\n", memo[i], temp);
        memo[i] = memo[i] > temp ? memo[i] : temp;
        counter += memo[i];
        printf("outer counter: %ld\n", counter);
        i++;
    }

    return counter;
}

// long countConfigsTest(int *adapters, int n) {

//     long counter = 0;
//     int configCounter = 0;

//     int pivot = 


// }

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    int *temp = charToIntArr(arr, n);

    int *adapters = calloc(n + 2, sizeof(int));

    for (int i = 0; i < n; i++) {
        adapters[i + 1] = temp[i];
    }

    adapters[0] = 0;
    adapters[n + 1] = maxFromArr(temp, n) + BUILT_IN;

    n = n + 2;

    //printf("%s\n", intArrayToString(adapters, n));

    int *joltages = calloc(3, sizeof(int));

    long *memo = calloc(n, sizeof(long));

    qsort(adapters, n, sizeof(int), intComp);

    //printf("%s\n", intArrayToString(adapters, n));

    printf(SEP);

    countJoltages(adapters, n, joltages);

    long configurations = countConfigs(adapters, n, memo);

    printf("\n%s", SEP);

    printf("Joltage differences: [1] -> %d | [2] -> %d | [3] -> %d || Result: %d\n", joltages[0], joltages[1], joltages[2], joltages[0] * joltages[2]);
    printf("Possible configurations: %ld\n", configurations);

    printf("%s\n", SEP);

    free(temp);
    free(adapters);
    free(joltages);
    free(memo);
    cleanMem(arr, MAX_LINES);

    return 0;
}