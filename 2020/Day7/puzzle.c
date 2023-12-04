#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define MAX_NAME 50
#define MAX_CONTENTS 2048
#define TEMP_SIZE 25

#define SEP "\033[0;31m----------------------------------------------------------------------------------------------------------------------------\n\033[0m"

struct Bag {
    char*   name;
    int     id;
    int**   contains;
    int     nContains;
    int     confirmed;
};

int** create2DintArray(int n, int m) {
    int** arr = calloc(n, sizeof(int*));
    for (int i = 0; i < n; i++) {
        arr[i] = calloc(m, sizeof(int));
    }
    return arr;
}

char* intArrayToString(int* arr, int n) {
    char* sArr = calloc(MAX_CONTENTS + 1, sizeof(char));
    strcpy(sArr, "[");
	for (int i = 0; i < n; i++) {
        char* temp = calloc((TEMP_SIZE + 1), sizeof(char));
		sprintf(temp, "%d%s", arr[i], (i == n - 1) ? "" : ", ");
        strcat(sArr, temp);
        free(temp);
	}
    strcat(sArr, "]");
    return sArr;
}

char* containsToString(int** arr, int n) {
    char* sArr = calloc(MAX_CONTENTS + 1, sizeof(char));
    strcpy(sArr, "[");
    for (int i = 0; i < n; i++) {
        char* temp = calloc(TEMP_SIZE + 1, sizeof(char));
        sprintf(temp, "BagID: %3d -> %d%s", arr[i][0], arr[i][1], (i == n - 1) ? "" : ", ");
        strcat(sArr, temp);
        free(temp);
    }
    strcat(sArr, "]");
    return sArr;
}

void cleanBags(struct Bag* bags, int n, int show) {
    for (int i = 0; i < n; i++) {
        if (show) printf("Cleaning bag %d!\n", i);
        free(bags[i].contains);
    }
    if (show) printf("Cleaning bag container!\n");
    free(bags);
}

void printBag(struct Bag* bag) {
    printf("Bag: %20s | BagID: %4d | Contains: %68s | %s\n", bag->name, bag->id, containsToString(bag->contains, bag->nContains), bag->confirmed ? "\e[0;32m\xE2\x9C\x93\e[0m" : "\e[0;31m\xE2\x9C\x98\e[0m");
}

void printBagNoContains(struct Bag* bag) {
    printf("Bag: %20s | BagID: %4d\n", bag->name, bag->id);
}

void printBags(struct Bag* bags, int n, int contains) {
    printf(SEP);
    for (int i = 0; i < n; i++) {
        if (contains) {
            printBag(&bags[i]);
        }
        else {
            printBagNoContains(&bags[i]);
        }
    }
    printf(SEP);
}

struct Bag createBag(char* name, int id) {
    struct Bag bag;
    bag.name = calloc(MAX_NAME + 1, sizeof(char));
    strcpy(bag.name, name);
    bag.id = id;
    bag.confirmed = 0;
    return bag;
}

void setBagContents(struct Bag* bag, int** contents, int n) {
    bag->contains = contents;
    bag->nContains = n;
}

int getBagID(struct Bag* bags, int n, char* name) {
    for (int i = 0; i < n; i++) {
        if (strcmp(bags[i].name, name) == 0) return i;
    }
    return -1;
}

int canHold(struct Bag* bags, int index, int queryID) {

    if (bags[index].nContains == 0 || bags[index].id == queryID) {
        return 0;
    }

    if (bags[index].confirmed) return 1;

    int confirmed = 0;

    for (int i = 0; i < bags[index].nContains; i++) {
        int id = bags[index].contains[i][0];
        // int count = bags[index].contains[i][1];

        if (id == queryID) {
            bags[index].confirmed = 1;
            confirmed = 1;
        }
        else {
            int holds = canHold(bags, id, queryID);
            if (holds) {
                bags[index].confirmed = 1;
                confirmed = 1;
            }
        }


    }

    return confirmed;
}

int countContainers(struct Bag* bags, int n, int queryID) {
    int counter = 0;

    for (int i = 0; i < n; i++) {

        int holds = canHold(bags, i, queryID);

        if (holds) bags[i].confirmed = 1;

        counter += holds;
    }

    return counter;
}

int stack(struct Bag* bags, int index) {
    int counter = 0;

    for (int i = 0; i < bags[index].nContains; i++) {

        int id = bags[index].contains[i][0];
        int count = bags[index].contains[i][1];

        counter += count + (count * stack(bags, id));

    }

    return counter;
}

int countStacked(struct Bag* bags, int n, int queryID) {
    return stack(bags, queryID);
}

int main(int argc, char** argv) {

    // READ FILE

    char** arr = readFile(argv[1]);
    int n = arrlen(arr);

    // CREATE BAG ARRAY

    struct Bag* bags = malloc(n * sizeof(struct Bag));

    // PARSE BAG NAMES

    for (int i = 0; i < n; i++) {

        char** bagData = split(arr[i], ' ');
        int nBagData = countChars(arr[i], ' ') + 1;

        char* name = calloc(MAX_NAME + 1, sizeof(char));
        strcpy(name, bagData[0]);
        strcat(name, " ");
        strcat(name, bagData[1]);

        int id = i;

        bags[i] = createBag(name, id);

        // printBag(&bags[i]);

        cleanMem(bagData, nBagData);

    }

    // CALCULATE CONTENTS

    for (int i = 0; i < n; i++) {

        char** bagData = split(arr[i], ' ');
        int nBagData = countChars(arr[i], ' ') + 1;

        int* contents = calloc(n, sizeof(int));
        int nContains = 0;

        for (int j = 4; j < nBagData; j += 4) {
            
            int count = atoi(bagData[j]);

            if (count == 0) {
                break;
            }
            else {

                char* bagName = calloc(MAX_NAME + 1, sizeof(char));
                strcpy(bagName, bagData[j + 1]);
                strcat(bagName, " ");
                strcat(bagName, bagData[j + 2]);

                int bagID = getBagID(bags, n, bagName);

                contents[bagID] = count;

                nContains++;

            }

        }

        int** contentsMin = create2DintArray(nContains, 2);
        int contentCounter = 0;

        for (int j = 0; j < n; j++) {
            if (contents[j] > 0) {
                contentsMin[contentCounter][0] = j;
                contentsMin[contentCounter][1] = contents[j];
                contentCounter++;
            }
            if (contentCounter >= nContains) break;
        }

        setBagContents(&bags[i], contentsMin, nContains);

        // printBag(&bags[i]);

        free(contents);
        cleanMem(bagData, nBagData);

    }

    // MAIN BIT

    char* query = "shiny gold";
    int queryID = getBagID(bags, n, query);

    int containers = countContainers(bags, n, queryID);
    int stacked = countStacked(bags, n, queryID);

    printBags(bags, n, 1);

    printf("Bags capable of holding '%s' (bagID: %d) bag: \e[1;34m%d\n\e[0m", query, queryID, containers);

    printf(SEP);

    printf("Bags held by bag '%s' (bagID: %d): \e[1;34m%d\n\e[0m", query, queryID, stacked);

    printf("%s\n", SEP);

    cleanMem(arr, MAX_LINES);
    cleanBags(bags, n, 0);

    return 0;
}