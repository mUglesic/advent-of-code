#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../../fileReader.h"

int getFuel(int mass) {
    return floor(mass / 3) - 2;
}

int sumExtraFuel(int fuel) {
    int sum = 0;
    int temp = fuel;
    int extra;
    while ((extra = getFuel(temp)) > 0) {
        sum += extra;
        temp = extra;
    }
    return sum;
}

int sumFuel(char** arr, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int fuel = getFuel(atoi(arr[i]));
        sum += fuel + sumExtraFuel(fuel);
    }
    return sum;
}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);
    int n = arrlen(arr);

    int fuel = sumFuel(arr, n);

    printf("Fuel requirements: %d\n", fuel);

    cleanMem(arr, MAX_LINES);

    return 0;
}