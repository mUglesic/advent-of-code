#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "../list.h"

#define LEN_MASK 36

long toDecimal(char *bin) {
    long n = 0;

    for (int i = 0; i < LEN_MASK; i++) {

        int exponent = LEN_MASK - i - 1;

        if (bin[i] == '1') {
            long curBitValue = pow(2, exponent);
            n += curBitValue;
        }


    }

    return n;
}

void rec(struct List *addresses, char *result, int index) {
    
    if (index >= LEN_MASK) {
        printf("%s\n", result);
        listAdd(addresses, createElement(toDecimal(result), 0));
        return;
    }

    if (result[index] == 'X') {

        char *temp = malloc((LEN_MASK + 1) * sizeof(char));

        strcpy(temp, result);

        temp[index] = '0';

        rec(addresses, temp, index + 1);

        temp[index] = '1';

        rec(addresses, temp, index + 1);

        free(temp);
        
    }
    else {
        rec(addresses, result, index + 1);
    }

}

int main() {

    char result[37] = "00000000000000000000000000000001X0XX";

    int xs = 3;
    long nAddresses = (long) pow(2, xs);

    struct List addresses = createList();

    rec(&addresses, result, 0);

    printf("\n\n");

    listPrintAll(&addresses);

    return 0;
}