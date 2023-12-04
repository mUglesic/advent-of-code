#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

void parseBusIDs(char **buses, int nBuses, int *busIDs) {

    int counter = 0;

    for (int i = 0; i < nBuses; i++) {
        if (strcmp(buses[i], "x") != 0) {
            busIDs[counter] = atoi(buses[i]);
            counter++;
        }
    }

}

int earliestDeparture(int time, int *busIDs, int nBusIDs) {

    printf("\nMy arrival: %d\n", time);

    int earliestID = 0, earliestTime = INT_MAX;

    for (int i = 0; i < nBusIDs; i++) {

        int closest = ceil((float) time / busIDs[i]) * busIDs[i];

        printf("\nBus ID: %d | Bus arrival: %d\n", busIDs[i], closest);

        if (closest < earliestTime) {
            earliestID = busIDs[i];
            earliestTime = closest;
        }

    }

    printf("\nEarliest departure time is %d using bus with ID %d\n", earliestTime, earliestID);

    return earliestID * (earliestTime - time);
}

long findSubsequent(char **buses, int nBuses, long timestamp, int index) {

    if (index >= nBuses) {
        return timestamp;
    }

    if (atoi(buses[index]) == 0) {
        char *num = copyFrom(buses[index], 0);
        int xNum = atoi(num);
        free(num);
        // printf("xNum: %d\n", xNum);
        return findSubsequent(buses, nBuses, timestamp + xNum, index + 1);
    }

    long nextTimestamp = ceil((double) timestamp / atoi(buses[index])) * atoi(buses[index]);

    if (nextTimestamp == timestamp + 1) {
        return findSubsequent(buses, nBuses, timestamp + 1, index + 1);
    }
    else {
        return 0;
    }
}

long matchingOffsets(char **buses, int nBuses, int n, int debug) {

    long matching = 0;
    long i = 5250000000000;
    int firstBus = atoi(buses[0]);

    while (matching == 0) {
        long timestamp = firstBus * i;
        matching = findSubsequent(buses, nBuses, timestamp, 1);
        if (debug && i % 1000 == 0)  printf("\nChecking timestamp %ld\n", timestamp);
        i++;
    }

    return matching - n + 1;
}

char **compactXs(char **buses, int nBuses) {

    char **new = malloc(MAX_BUFF * sizeof(char *));

    int j = 0;

    for (int i = 0; i < nBuses; i++) {

        int counter = 0;
        int x = 0;

        while (atoi(buses[i]) == 0) {
            counter++;
            i++;
            x = 1;
        }

        char *element = malloc(TEMP_SIZE * sizeof(char));

        if (counter > 0) {
            sprintf(element, "x%d", counter);
        }
        else {
            strcpy(element, buses[i]);
        }

        new[j] = element;
        j++;

        if (x) i--;

    }

    new[j] = NULL;

    return new;
}

int main(int argc, char **argv) {

    // READING AND PARSING

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    int time = atoi(arr[0]);

    char **buses = split(arr[1], ',');
    int nBuses = (countChars(arr[1], ',') + 1);

    int nBusIDs = nBuses - countChars(arr[1], 'x');
    int *busIDs = malloc(nBusIDs * sizeof(int));

    parseBusIDs(buses, nBuses, busIDs);

    // MAIN

    printf(SEP);

    // PART 1

    int departure = earliestDeparture(time, busIDs, nBusIDs);

    printf("\n%s", SEP);

    // PART 2

    char **newBuses = compactXs(buses, nBuses);
    int newNBuses = arrlen(newBuses);

    print2DArray(newBuses);
    printf("array size: %d\n", newNBuses);

    long earliestMatchingOffsets = matchingOffsets(newBuses, newNBuses, nBuses, 0);

    printf("\n%s", SEP);

    printf("ID * WAIT_TIME = %d | Matching offsets: %ld\n", departure, earliestMatchingOffsets);

    printf("%s\n", SEP);

    // GARBAGE

    free(busIDs);

    cleanMem(newBuses, MAX_BUFF);
    cleanMem(buses, nBuses);
    cleanMem(arr, MAX_LINES);

    return 0;
}