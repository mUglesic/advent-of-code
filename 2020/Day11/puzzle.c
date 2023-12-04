#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

char **createCopyOf2DArray(char **arr, int n, int m) {

    char **new = create2DcharArray(n, m);

    for (int i = 0; i < n; i++) {

        strcpy(new[i], arr[i]);

    }

    return new;
}

void copy2DArray(char **dest, char **src, int n) {
    for (int i = 0; i < n; i++) {
        strcpy(dest[i], src[i]);
    }
}

int diff(char **arr1, char **arr2, int n) {
    // SAME: RETURNS 0
    // DIFFERENT: RETURNS 1

    for (int i = 0; i < n; i++) {
        if (strcmp(arr1[i], arr2[i]) != 0) return 1;
    }

    return 0;
}

int checkVisibleNeighbor(char **arr, int n, int m, int ii, int jj, int iDir, int jDir) {
    int i = ii + iDir, j = jj + jDir;
    while ((i >= 0 && i < n) && (j >= 0 && j < m)) {
        switch (arr[i][j]) {
            case 'L':
                return 0;
            case '#':
                return 1;
            default:
                break;
        }
        i += iDir;
        j += jDir;
    }
    return 0;
}

int countNeighbors(char **arr, int n, int m, int ii, int jj) {
    int counter = 0;
    for (int i = ii - 1; i <= ii + 1; i++) {
        for (int j = jj - 1; j <= jj + 1; j++) {
            if (i == ii && j == jj) continue;
            if (!((i < 0 || i >= n) || (j < 0 || j >= m))) {
                counter += (arr[i][j] == '#');
            }
        }
    }
    return counter;
}

int countVisibleNeighbors(char **arr, int n, int m, int ii, int jj) {
    int counter = 0;
    counter += checkVisibleNeighbor(arr, n, m, ii, jj,  1,  1); // UP RIGHT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj,  1,  0); // RIGHT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj,  1, -1); // DOWN RIGHT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj,  0, -1); // DOWN
    counter += checkVisibleNeighbor(arr, n, m, ii, jj, -1, -1); // DOWN LEFT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj, -1,  0); // LEFT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj, -1,  1); // UP LEFT
    counter += checkVisibleNeighbor(arr, n, m, ii, jj,  0,  1); // UP
    return counter;
}

void enforceRules(char **main, char **copy, int n, int m) {

    copy2DArray(copy, main, n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {

            char seat = copy[i][j];

            int occupiedNeighbors = countVisibleNeighbors(copy, n, m, i, j);

            switch (seat) {
                case 'L':
                    // EMPTY
                    main[i][j] = (occupiedNeighbors == 0) ? '#' : 'L';
                    break;
                case '#':
                    // OCCUPIED
                    main[i][j] = (occupiedNeighbors >= 5) ? 'L' : '#';
                    break;
                default:
                    //FLOOR
                    break;
            }

        }
    }


}

int fillSeats(char **main, char **copy, int n, int m, int debug) {
    
    int counter = 0;

    enforceRules(main, copy, n, m);

    if (debug) {
        printf("\n");
        print2DArray(main);
    }
    else printf("\n\e[0;33mPOGGY\e[0m\n");

    while (diff(main, copy, n)) {
        enforceRules(main, copy, n, m);
        if (debug) {
            printf("\n");
            print2DArray(main);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            counter += (main[i][j] == '#');
        }
    }

    return counter;
}

int main(int argc, char **argv) {

    char **main = readFile(argv[1]);
    int n = arrlen(main);
    int m = strlen(main[0]);

    char **copy = createCopyOf2DArray(main, n, m);

    printf(SEP);

    int occupied = fillSeats(main, copy, n, m, 0);

    printf("\n%s", SEP);

    printf("Occupied seats: %d\n", occupied);

    printf("%s\n", SEP);

    cleanMem(main, MAX_LINES);
    cleanMem(copy, n);

    return 0;
}
