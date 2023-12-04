#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define DIFF 7

int comp(const void *el1, const void *el2) {
    int f = *((int *) el1);
    int s = *((int *) el2);
    return (f > s) - (f < s);
}

void printArray(int *arr, int n) {
	printf("[");
	for (int i = 0; i < n; i++) {
		printf("%d%s", arr[i], (i == n - 1) ? "" : ", ");
	}
	printf("]\n");
}

int getRow(char *key, int n, int i, int start, int end) {

    if (i >= n) {
        // printf("start: %d, end: %d\n", start, end);
        return end;
    }

    char c = key[i];

    float middle = (start + end) / 2.0;
    // printf("key: %c | %f\n", c, middle);

    if (c == 'F' || c == 'L') {
        return getRow(key, n, i + 1, start, (int) floor(middle));
    }
    else if (c == 'B' || c == 'R') {
        // printf("upper\n");
        return getRow(key, n, i + 1, (int) ceil(middle), end);
    }

    return -1;

}

int getCol(char *key, int n, int i, int start, int end) {
    return getRow(key, n, i, start, end);
}

int findSeat(char *key) {

    printf("Key: %s\n", key);

    char *rowKey = copyTo(key, DIFF);
    char *colKey = copyFrom(key, DIFF - 1);

    printf("rowKey: %s | colKey: %s\n", rowKey, colKey);

    int row = getRow(rowKey, 7, 0, 0, 127);
    int col = getCol(colKey, 3, 0, 0, 7);

    int seatID = row * 8 + col;

    printf("   row: %7d |    col: %3d |   seatID: %d\n\n", row, col, seatID);

    return seatID;    
}

int *findSeats(char **arr, int n) {
    int *seatIDs = calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) {
        seatIDs[i] = findSeat(arr[i]);
    }
    return seatIDs;
}

int maxFromArr(int *arr, int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        max = max < arr[i] ? arr[i] : max;
    }
    return max;
}

int findMissing(int *arr, int n) {
    int cur = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] != cur + 1) return cur + 1;
        cur = arr[i];
    }
    return -1;
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    int *seatIDs = findSeats(arr, n);

    qsort(seatIDs, n, sizeof(int), comp);

    // printArray(seatIDs, n);

    int max = maxFromArr(seatIDs, n);
    int myID = findMissing(seatIDs, n);

    printf("Max seatID: %d | My seatID: %d\n", max, myID);

    free(seatIDs);
    cleanMem(arr, MAX_LINES);

    return 0;
}