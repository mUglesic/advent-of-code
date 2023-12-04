#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../fileReader.h"
#include "../stringManipulator.h"
#include "../list.h"

char **setArray(char **arr, int start, int end) {
    char **newArr = malloc((end - start) * sizeof(char *));
    for (int i = start; i < end; i++) {
        newArr[i - start] = arr[i];
    }
    return newArr;
}

void cleanArray(int **arr, int n) {
    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);
}

int **parseRules(char **rules, int nRules) {
    int **newRules = malloc(nRules * sizeof(int *));

    for (int i = 0; i < nRules; i++) {
        newRules[i] = malloc(4 * sizeof(int));

        char **splitRule = split(rules[i], ':');

        char *temp = copyFrom(splitRule[1], 0);

        char **limits = split(temp, ' ');

        char **limit1 = split(limits[0], '-');
        char **limit2 = split(limits[2], '-');

        printf("Rule: %s -> %s | %s -> %s\n", limit1[0], limit1[1], limit2[0], limit2[1]);

        for (int j = 0; j < 4; j++) {
            newRules[i][j] = (j < 2) ? atoi(limit1[j % 2]) : atoi(limit2[j % 2]);
        }

        free(temp);
        cleanMem(splitRule, 2);
        cleanMem(limits, 3);
        cleanMem(limit1, 2);
        cleanMem(limit2, 2);

    }

    printf("Successfully parsed rules!\n");

    return newRules;
}

int **parseTickets(char **tickets, int nTickets) {
    int **newTickets = malloc(nTickets * sizeof(int *));

    for (int i = 0; i < nTickets; i++) {
        char **splitTicket = split(tickets[i], ',');
        int nSplitTicket = countChars(tickets[i], ',') + 1;

        newTickets[i] = malloc(nSplitTicket * sizeof(int));

        for (int j = 0; j < nSplitTicket; j++) {
            newTickets[i][j] = atoi(splitTicket[j]);
        }

        cleanMem(splitTicket, nSplitTicket);

    }

    printf("Successfully parsed tickets!\n");

    return newTickets;
}

int *getTicketLengths(char **tickets, int nTickets) {
    int *ticketLengths = malloc(nTickets * sizeof(int));

    for (int i = 0; i < nTickets; i++) {
        ticketLengths[i] = countChars(tickets[i], ',') + 1;
    }

    printf("Got ticket lengths!\n");

    return ticketLengths;
}

int isInvalid(int **rules, int nRules, int ticket) {
    for (int i = 0; i < nRules; i++) {
        for (int j = 0; j < 2; j++) {
            int min = rules[i][j * 2];
            int max = rules[i][j * 2 + 1];
            if (ticket >= min && ticket <= max) {
                printf("Ticket %d is valid!\n", ticket);
                return 0;
            }
        }
    }
    printf("Ticket %d is invalid!\n", ticket);
    return 1;
}

void findInvalidTickets(int **rules, int nRules, int **tickets, int nTickets, int *ticketLengths, struct List *invalidTickets) {
    for (int i = 0; i < nTickets; i++) {
        for (int j = 0; j < ticketLengths[i]; j++) {
            if (isInvalid(rules, nRules, tickets[i][j])) {
                listAdd(invalidTickets, createElement(0, tickets[i][j]));
                printf("Ticket %d added to list!\n", tickets[i][j]);
            }
        }
    }
}

int sumInvalidTickets(char **rules, int nRules, char **tickets, int nTickets) {

    int **newRules = parseRules(rules, nRules);

    int **newTickets = parseTickets(tickets, nTickets);
    int *ticketLengths = getTicketLengths(tickets, nTickets);

    struct List invalidTickets = createList();

    findInvalidTickets(newRules, nRules, newTickets, nTickets, ticketLengths, &invalidTickets);

    int sum = listSumElements(&invalidTickets);

    printf("Summed up invalid tickets!\n");

    cleanArray(newRules, nRules);
    cleanArray(newTickets, nTickets);
    free(ticketLengths);

    return sum;
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    int nRules = 0;

    while (strcmp(arr[nRules], "") != 0) { nRules++; }

    char **rules = setArray(arr, 0, nRules);

    printf("Read rules!\n");

    char *myTicket = arr[nRules + 2];

    char **tickets = setArray(arr, nRules + 5, n);
    int nTickets = n - (nRules + 5);

    printf("Read tickets!\n");

    int sum = sumInvalidTickets(rules, nRules, tickets, nTickets);

    printf("Sum of invalid ticket fields: %d\n", sum);

    free(rules);
    free(tickets);
    cleanMem(arr, MAX_LINES);

    return 0;
}