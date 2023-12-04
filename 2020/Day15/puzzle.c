#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"
#include "../list.h"

#define N 100000

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);

    char **starting = split(arr[0], ',');
    int nStarting = countChars(arr[0], ',') + 1;

    struct List spoken = createList();

    int prev = 0;

    for (int i = 0; i < nStarting; i++) {
        listAdd(&spoken, createElement(atoi(starting[i]), i));
        prev = atoi(starting[i]);
    }

    for (int i = nStarting; i < N; i++) {
        
        int prevIndex = listGetIndex(&spoken, createElement(prev, 0));

        // printf("%d %s\n", prev, (prevIndex == -1 || prevIndex < nStarting) ? "not spoken" : "spoken");

        if (prevIndex == -1 || i == nStarting) {
            // NOT SPOKEN EVER
            int zeroIndex = listGetIndex(&spoken, createElement(0, 0));
            if (zeroIndex == -1) {
                listAdd(&spoken, createElement(0, i));
            }
            // else {
            //     printf("zeroindex: %d\n", zeroIndex);
            //     listGetByIndex(&spoken, zeroIndex)->next->el->value = i;
            // }
            if (i % 10000 == 0) printf("%d. %d\n", i + 1, 0);
            prev = 0;
        }
        else {
            struct ListElement *element = listGetByIndex(&spoken, prevIndex);
            int nextNum = i - 1 - element->next->el->value;
            if (i % 10000 == 0) printf("%d. %d\n", i + 1, nextNum);
            if (listGetIndex(&spoken, createElement(nextNum, 0)) == -1) {
                listAdd(&spoken, createElement(nextNum, i));
            }
            //listAdd(&spoken, createElement(nextNum, i));
            element->next->el->value = i - 1;
            prev = nextNum;
        }

        // listPrintAll(&spoken);

    }

    // listPrintAll(&spoken);

    cleanMem(starting, nStarting);
    cleanMem(arr, MAX_LINES);

    return 0;
}