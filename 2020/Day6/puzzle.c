#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"

int getIndex(char c) {
    return c - 'a';
}

void countAnswers(int* answers, char* person) {

    for (int i = 0; i < strlen(person); i++) {
        answers[getIndex(person[i])] += 1;
    }

}

int sumAnswers(int* answers, int n) {
    int sum = 0;
    for (int i = 0; i < 26; i++) {
        if (answers[i] >= n) sum++;
    }
    printf("Mid sum: %d\n", sum);
    return sum;
}

int collectAnswers(char** arr, int n) {

    int sum = 0;

    for (int i = 0; i < n; i++) {

        int* answers = calloc(26, sizeof(int));

        char* person = arr[i];

        int groupCounter = 0;

        while (strcmp(person, "") != 0) {
            printf("person: %s\n", person);
            countAnswers(answers, person);
            groupCounter++;
            i++;
            if (i >= n) break;
            person = arr[i];
        }

        sum += sumAnswers(answers, groupCounter);

        free(answers);

    }

    return sum;

}

int main(int argc, char** argv) {

    char** arr = readFile(argv[1]);
    int n = arrlen(arr);

    int sum = collectAnswers(arr, n);

    printf("Sum: %d\n", sum);

    cleanMem(arr, MAX_LINES);
    return 0;
}