#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFF 2048
#define MAX_LINES 2560

char** create2DcharArray(int n, int m) {
  char **arr = malloc(n * sizeof(char *));
  for (int i = 0; i < n; i++) {
    arr[i] = malloc((m + 1) * sizeof(char));
  }
  return arr;
}

void printn2DArray(char **arr, int n) {
  for (int i = 0; i < n; i++) {
	  printf("%s\n", arr[i]);
  }
}

void print2DArray(char **arr) {
  char *line;
  int i = 0;
  while ((line = arr[i]) != NULL) {
	printf("%s\n", line);  
	i++;
  }
}

int arrlen(char **arr) {
  char *line;
  int i = 0;
  while ((line = arr[i]) != NULL) {
	i++;
  }
  return i;
}

char* readLine(FILE *f, int maxLen) {
  char* buff = malloc((maxLen + 1) * sizeof(char));
  char c;
  int len = 0;
  while ((c = fgetc(f)) != '\n') {
    if (c == EOF) {
      printf("EOF reached!\n");
      free(buff);
      return NULL;
    }
    buff[len] = c;
    len++;
    if (len == maxLen) {
      printf("Line length exceeded $maxLen: line shortened\n");
      break;
    }
  }
  buff[len] = '\0';
  char* res = malloc((len + 1) * sizeof(char));
  strcpy(res, buff);
  free(buff);
  return res;
}

void cleanMem(char **arr, int n) {
  for (int i = 0; i < n; i++) {
    free(arr[i]);
  }
  free(arr);
}

char** readFile(char* path) {

  FILE *f;
  char *line;

  printf("\nAttempting to open file '%s'\n", path);
  f = fopen(path, "r");

  if (f == 0) {
    printf("ERROR\n");
    exit(-1);
  }
  
  printf("\e[0;32mSuccessfully opened file!\e[0m\n");

  line = readLine(f, MAX_BUFF);
  
  printf("Creating line array...\n");

  char **arr = create2DcharArray(MAX_LINES, strlen(line));
  arr[0] = line;
  int n = 1;
  
  printf("Reading lines...\n");

  while ((line = readLine(f, MAX_BUFF)) != NULL) {
    arr[n] = line;
    n++;
  }
  
  arr[n] = NULL;
  
  printf("Read %d lines!\n", n);
  
  printf("Closing file...\n\n");

  fclose(f);
  
  line = malloc(2 * sizeof(char));
  free(line);
  // cleanMem(arr, MAX_LINES);

  return arr;
}