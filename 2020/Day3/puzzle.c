#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFF 255
#define MAX_LINES 512

char** create2DArray(int n, int m) {
  char **arr = malloc(n * sizeof(char *));
  for (int i = 0; i < n; i++) {
    arr[i] = malloc(m * sizeof(char));
  }
  return arr;
}

void print2DArray(char **arr, int n) {
  for (int i = 0; i < n; i++) {
    printf("%s\n", arr[i]);
  }
}

char* readLine(FILE *f, int maxLen) {
  char* buff = malloc(maxLen * sizeof(char));
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
  char* res = malloc(len * sizeof(char));
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

int countTrees(char** arr, int n, int x, int y) {

  // printf("arr len: %d\n", n);
  
  int i = 0; int j = 0;

  int counter = 0;

  while (i < n) {

    j %= strlen(arr[i]);

    char c = arr[i][j];

    if (c == '#') {
      counter++;
    }

    // printf("char at: %d, %d = %c\n", i, j, arr[i][j]);

    i += y;
    j += x;
  }

  return counter;
}

int main(int argc, char **argv) {

  FILE *f;
  char *input = argv[1];
  char *line;

  f = fopen(input, "r");

  if (f == 0) {
    printf("ERROR\n");
    return -1;
  }

  line = readLine(f, 255);

  char **arr = create2DArray(MAX_LINES, strlen(line));
  arr[0] = line;
  int n = 1;

  while ((line = readLine(f, MAX_BUFF)) != NULL) {
    arr[n] = line;
    n++;
  }

  // print2DArray(arr, n);

  // int treesHit = countTrees(arr, n, 3, 1);
  long treesHit = countTrees(arr, n, 1, 1) * countTrees(arr, n, 3, 1) * countTrees(arr, n, 5, 1) * countTrees(arr, n, 7, 1) * countTrees(arr, n, 1, 2);

  printf("Trees hit: %ld\n", treesHit);

  fclose(f);
  free(line);
  cleanMem(arr, MAX_LINES);

  return 0;
}