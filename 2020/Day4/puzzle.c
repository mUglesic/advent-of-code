// #include <sys/types.h>
// #include <sys/stat.h>
// #include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "../fileReader.h"

void printArray(int *arr, int n) {
	printf("[");
	for (int i = 0; i < n; i++) {
		printf("%d%s", arr[i], (i == n - 1) ? "" : ", ");
	}
	printf("]\n");
}

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

int getFieldIndex(char *s) {
	if (strcmp(s, "byr") == 0) {
		return 0;
	}
	else if (strcmp(s, "iyr") == 0) {
		return 1;
	}
	else if (strcmp(s, "eyr") == 0) {
		return 2;
	}
	else if (strcmp(s, "hgt") == 0) {
		return 3;
	}
	else if (strcmp(s, "hcl") == 0) {
		return 4;
	}
	else if (strcmp(s, "ecl") == 0) {
		return 5;
	}
	else if (strcmp(s, "pid") == 0) {
		return 6;
	}
	else if (strcmp(s, "cid") == 0) {
		return 7;
	}
}

int arrcmp(int *arr1, int *arr2, int n) {
	for (int i = 0; i < n; i++) {
		if (arr1[i] != arr2[i]) {
			return 0;
		}
	}
	return 1;
}

int checkaTof(char c) {
	return c >= 'a' && c <= 'f';
}

int checkCredentials(int *passportFields, int n) {
	int northPoleCreds[8] = {1, 1, 1, 1, 1, 1, 1, 0};
	int passportCreds[8] = {1, 1, 1, 1, 1, 1, 1, 1};
	return arrcmp(passportFields, northPoleCreds, n) || arrcmp(passportFields, passportCreds, n);
}

int checkHeight(char *value) {
	char *cm = strstr(value, "cm");
	char *in = strstr(value, "in");
	char *h;
	int height;
	if (cm) {
		h = copyTo(value, findChar(value, 'c'));
		height = atoi(h);
		return height >= 150 && height <= 193;
	}
	else if (in) {
		h = copyTo(value, findChar(value, 'i'));
		height = atoi(h);
		return height >= 59 && height <= 76;
	}
	else {
		return 0;
	}
}

int checkHairColor(char *col) {
	int leadingHash = col[0] == '#';
	for (int i = 1; i < strlen(col); i++) {
		if (!checkaTof(col[i]) && !isdigit(col[i])) return 0;
	}
	return leadingHash && strlen(col) == 7;
}

int checkEyeColor(char *col) {
	return strcmp(col, "amb") == 0 || strcmp(col, "blu") == 0 || strcmp(col, "brn") == 0 || strcmp(col, "gry") == 0 || strcmp(col, "grn") == 0 || strcmp(col, "hzl") == 0 || strcmp(col, "oth") == 0;
}

int checkValue(int index, char *value) {
	int year;
	switch(index) {
		case 0:
			year = atoi(value);
			return year >= 1920 && year <= 2002;
		case 1:
			year = atoi(value);
			return year >= 2010 && year <= 2020;
		case 2:
			year = atoi(value);
			return year >= 2020 && year <= 2030;
		case 3:
			return checkHeight(value);
		case 4:
			return checkHairColor(value);
		case 5:
			return checkEyeColor(value);
		case 6:
			return strlen(value) == 9 && atoi(value);
		default:
			return 1;
	}
}

int isValid(char *passport) {

	int *passportFields = calloc(8, sizeof(int));

	char *token;

	token = strtok(passport, " ");

	while (token != NULL) {

		printf("token: %s\n", token);

		int colonIndex = findChar(token, ':');
		char *key = copyTo(token, colonIndex);
		char *value = copyFrom(token, colonIndex);

		if (checkValue(getFieldIndex(key), value)) passportFields[getFieldIndex(key)] = 1;

		printf("\tkey: %s | value: %s\n", key, value);

		token = strtok(NULL, " ");

	}

	printArray(passportFields, 8);

	int valid = checkCredentials(passportFields, 8);

	free(passportFields);

	return valid;
}

int checkPassports(char **arr, int n) {

	char *passport = calloc(MAX_BUFF, sizeof(char));
	int validCounter = 0;

	for (int i = 0; i < n; i++) {

		char *line = arr[i];

		if (strcmp(line, "") == 0 || i == n - 1) {

			if (i == n - 1) {
				strcat(passport, line);
			}

			printf("%s\n", passport);
			
			// if (isValid(passport)) {
			// 	validCounter++;
			// }

			validCounter += isValid(passport);

			passport = calloc(MAX_BUFF, sizeof(char));

		}
		else {
			strcat(passport, line);
			strcat(passport, " ");
		}

	}

	free(passport);

	return validCounter;

}

int main(int argc, char **argv) {

	// DEBUG

	// int bak, new;

	// fflush(stdout);
	// bak = dup(1);
	// new = open("result.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
	// dup2(new, 1);
	// close(new);

	// END

	char *path = argv[1];
	char **arr = readFile(path);

	int n = arrlen(arr);

	int valid = checkPassports(arr, n);

	printf("Num of valid passports: %d\n", valid);

	// printf("%s\n", strtok(arr[0], " "));

	cleanMem(arr, MAX_LINES);

	// DEBUG

	// fflush(stdout);
	// dup2(bak, 1);
	// close(bak);

	// END

	return 0;

}