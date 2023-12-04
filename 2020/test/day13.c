#include <stdio.h>
#include <stdlib.h>

int main() {

    int t[74] = {19, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 37, 0, 0, 0, 0, 0, 821, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 463, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23};
    int n = 74;

    long i = 1;

    while (1) {
        
        long x = t[0] * i;

        if (i % 1000000000 == 0) printf("%ld\n", x);

        int solved = 1;

        for (long j = 0; j < n; j++) {
            if (t[j] == 0) continue;
            if ((x + j) % t[j] != 0) {
                solved = 0;
                break;
            }
        }

        if (solved) printf("%ld\n", x);

        i++;

    }

    return 0;
}