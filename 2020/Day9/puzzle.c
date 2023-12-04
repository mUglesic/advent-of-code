#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define PREAMBLE_LENGTH 25

int checkRules(char **arr, int n, int index) {
    int cur = atoi(arr[index]);

    for (int i = index - PREAMBLE_LENGTH; i < index; i++) {
        for (int j = index - PREAMBLE_LENGTH; j < index; j++) {

            if (i == j) continue;

            if (cur == (atoi(arr[i]) + atoi(arr[j]))) {
                return 1;
            }

        }
    }

    return 0;

}

int findSum(char **arr, int n, int start, int query) {

    int sum = 0;
    int nSum = 0;

    int smallest = atoi(arr[start]), largest = atoi(arr[start]);

    int found = 0;

    for (int i = start; i < n; i++) {
        sum += atoi(arr[i]);
        nSum++;

        smallest = smallest < atoi(arr[i]) ? smallest : atoi(arr[i]);
        largest = largest > atoi(arr[i]) ? largest : atoi(arr[i]);

        if (sum == query && nSum > 1) {
            printf("\nSmallest: %d | Largest: %d\n", smallest, largest);
            found = 1;
            break;
        }
        else if (sum > query) {
            break;
        }

    }

    return found ? smallest + largest : -1;
}

int findNumber(char **arr, int n) {

    int thatNumber = -1;
    
    for (int i = PREAMBLE_LENGTH; i < n; i++) {

        if (!checkRules(arr, n, i)) {
            printf("\nNumber '%s' \e[0;31mdoesn't follow\e[0m the rule!\n", arr[i]);
            thatNumber = atoi(arr[i]);
            break;
        }

        printf("\nNumber '%s' \e[0;32mfollows\e[0m the rule!\n", arr[i]);

    }

    int sum = -1;

    for (int i = 0; i < n; i++) {

        sum = findSum(arr, n, i, thatNumber);

        if (sum > -1) {
            break;
        }

    }

    return sum;
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    printf(SEP);

    int first = findNumber(arr, n);

    printf("\n%s", SEP);

    printf("Result: %d\n", first);

    printf("%s\n", SEP);

    cleanMem(arr, MAX_LINES);

    return 0;
}