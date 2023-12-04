#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include "../../fileReader.h"
#include "../../stringManipulator.h"

#define MAX_INTERSECTIONS 512

int** create2DintArray(int n, int m) {
    int** arr = calloc(n, sizeof(int*));
    for (int i = 0; i < n; i++) {
        arr[i] = calloc(m, sizeof(int));
    }
    return arr;
}

int** getWireSegments(char* wire) {

    int n = countChars(wire, ',') + 1;
    char** dirs = split(wire, ',');

    int** coords = create2DintArray(n, 4);
    int prevX = 0, prevY = 0, curX = 0, curY = 0;

    for (int i = 0; i < n; i++) {
        char dir = dirs[i][0];
        int val = atoi(copyFrom(dirs[i], 0));

        switch(dir) {
            case 'U':
                curY += val;
                break;
            case 'D':
                curY -= val;
                break;
            case 'L':
                curX -= val;
                break;
            case 'R':
                curX += val;
                break;
        }

        printf("Direction: %c | Distance: %d\n", dir, val);

        printf("x1: %d, y1: %d | x2: %d, y2: %d\n", prevX, prevY, curX, curY);

        coords[i][0] = prevX;
        coords[i][1] = prevY;
        coords[i][2] = curX;
        coords[i][3] = curY;

        prevX = curX;
        prevY = curY;
    }

    printf("----------------------------------------------\n");

    cleanMem(dirs, n);

    return coords;

}

int findMin(int* arr, int n) {
    int m = arr[0];
    for (int i = 1; i < n; i++) {
        m = min(arr[i], m);
    }
    return m;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int onLine(int px, int py, int x1, int y1, int x2, int y2) {
    return (px >= min(x1, x2) && px <= max(x1, x2)) && (py >= min(y1, y2) && py <= max(y1, y2));
}

int* findIntersection(int* l1, int* l2) {

    int x1 = l1[0], y1 = l1[1], x2 = l1[2], y2 = l1[3];

    int x3 = l2[0], y3 = l2[1], x4 = l2[2], y4 = l2[3];

    int denominator = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));

    if (denominator == 0) {
        return NULL;
    }

    int px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator;
    int py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator;

    if (onLine(px, py, x1, y1, x2, y2) && onLine(px, py, x3, y3, x4, y4)) {
        int* point = calloc(2, sizeof(int));
        point[0] = px;
        point[1] = py;
        return point;
    }
    else {
        return NULL;
    }

}

int countSteps(int** wire, int n, int x, int y) {
    int stepCounter = 0;
    int* startEnd;
    for (int i = 0; i < n; i++) {
        startEnd = wire[i];
        int x1 = startEnd[0], y1 = startEnd[1], x2 = startEnd[2], y2 = startEnd[3];
        if (onLine(x, y, x1, y1, x2, y2)) {
            if (x == x1 && x == x2) {
                stepCounter += abs(y - y1);
            }
            else if (y == y1 && y == y2) {
                stepCounter += abs(x - x1);
            }
            return stepCounter;
        }
        else {
            stepCounter += abs(x1 - x2) + abs(y1 - y2);
        }
    }
    return 0;  
}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);

    int n1 = countChars(arr[0], ',') + 1;
    int n2 = countChars(arr[1], ',') + 1;

    int** wire1 = getWireSegments(arr[0]);
    int** wire2 = getWireSegments(arr[1]);

    printf("Wire 1:\n");
    for (int i = 0; i < n1; i++) {
        printf("Start: %d, %d | End: %d, %d\n", wire1[i][0], wire1[i][1], wire1[i][2], wire1[i][3]);
    }

    printf("Wire 2:\n");
    for (int i = 0; i < n2; i++) {
        printf("Start: %d, %d | End: %d, %d\n", wire2[i][0], wire2[i][1], wire2[i][2], wire2[i][3]);
    }

    int minDistance = INT_MAX;

    int** intersections = create2DintArray(MAX_INTERSECTIONS, 2);
    int nInter = 0;

    for (int i = 0; i < n1; i++) {
        for (int j = 1; j < n2; j++) {
            int* intersection = findIntersection(wire1[i], wire2[j]);
            if (intersection){
                printf("Intersection at: %d, %d\n", intersection[0], intersection[1]);
                intersections[nInter][0] = intersection[0];
                intersections[nInter][1] = intersection[1];
                nInter++;
                minDistance = min(minDistance, abs(intersection[0]) + abs(intersection[1])); 
            }
            free(intersection);
        }
    }

    int* stepCount = calloc(nInter, sizeof(int));

    for (int i = 0; i < nInter; i++) {
        int x = intersections[i][0];
        int y = intersections[i][1];

        int s1 = countSteps(wire1, n1, x, y);
        int s2 = countSteps(wire2, n2, x, y);

        stepCount[i] = s1 + s2;
        // printf("Intersection %d: %d, %d\n", i + 1, intersections[i][0], intersections[i][1]);
    }

    printf("Minimum steps required: %d\n", findMin(stepCount, nInter));
    printf("Minimum Manhattan distance: %d\n", minDistance);

    free(stepCount);

    cleanMem(wire1, n1);
    cleanMem(wire2, n2);
    cleanMem(intersections, MAX_INTERSECTIONS);
    cleanMem(arr, MAX_LINES);

    return 0;
}