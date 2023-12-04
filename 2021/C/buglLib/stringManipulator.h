#include <stdlib.h>
#include <string.h>

#define MAX_LEN 512
#define TEMP_SIZE 10
#define SEP "\e[0;31m----------------------------------------------------------------------------------------------------------------------------\n\e[0m"

char *copyTo(char *s, int n) {
	char* cpy = malloc((n + 1) * sizeof(char));
	for (int i = 0; i < n; i++) {
		cpy[i] = s[i];
	}
	cpy[n] = '\0';
	return cpy;
}

char *copyFrom(char *s, int n) {
	int nn = strlen(s) - n - 1;
	// printf("nn: %d\n", nn);
	char* cpy = malloc((nn + 1) * sizeof(char));
	for (int i = 0; i < nn; i++) {
		cpy[i] = s[i + n + 1];
	}
	cpy[nn] = '\0';
	return cpy;
}

int findChar(char *s, char c) {
	for (int i = 0; i < strlen(s); i++) {
		if (s[i] == c) {
			return i;
		}
	}
	return -1;
}

int countChars(char* s, char c) {
    int counter = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == c) {
            counter++;
        }
    }
    return counter;
}

char** split(char* s, char c) {
	int n = countChars(s, c) + 1;
    char** newS = calloc(n, sizeof(char*));
    char* buff = calloc(255, sizeof(char));
    int curIndex = 0;
    char curChar;

    for (int i = 0; i < n; i++) {

        while((curChar = s[curIndex]) != c && curIndex < strlen(s)) {

            strncat(buff, &curChar, 1);

            curIndex++;

        }

        newS[i] = malloc((strlen(buff) + 1) * sizeof(char));
		
		strcpy(newS[i], buff);

        buff = calloc(255, sizeof(char));
        curIndex++;

    }

    free(buff);

    return newS;
}

char* intArrayToString(int* arr, int n) {
    char* sArr = calloc(MAX_LEN + 1, sizeof(char));
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