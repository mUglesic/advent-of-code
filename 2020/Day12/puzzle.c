#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../fileReader.h"
#include "../stringManipulator.h"

#define PI 3.14159265

struct Vector {
    int x;
    int y;
    int dir;
};

void setPosition(struct Vector *v, int x, int y, int dir) {
    v->x = x;
    v->y = y;
    v->dir = dir;
}

void add(struct Vector *v1, struct Vector *v2) {
    v1->x += v2->x;
    v1->y += v2->y;
}

void multn(struct Vector *v, int n) {
    v->x *= n;
    v->y *= n;
}

void rotate(struct Vector *v, int angle) {
    int x1 = v->x, y1 = v->y;
    float a = angle * (PI / 180);
    float x2 = cos(a) * x1 - sin(a) * y1;
    //printf("\n%f\n", a);
    float y2 = sin(a) * x1 + cos(a) * y1;
    //printf("\n%f, %f\n", x2, y2);
    setPosition(v, round(x2), round(y2), 0);
}

void printPos(struct Vector *v) {
    printf("Vector position: %d, %d | Direction: %d\n", v->x, v->y, v->dir);
}

char translateDir(int dir) {
    return dir == 0 ? 'E' : (dir == 90 ? 'S' : (dir == 180 ? 'W' : 'E'));
}

char *getDirection(char dir) {
    return dir == 'N' ? "NORTH" : (dir == 'S' ? "SOUTH" : (dir == 'E' ? "EAST" : "WEST"));
}

void move(struct Vector *v, char dir, int amount) {
    printf("\nMoving waypoint by \e[0;35m%d\e[0m in direction \e[0;33m%s\e[0m\n", amount, getDirection(dir));
    switch (dir) {
        case 'N':
            v->y = v->y - amount;
            break;
        case 'S':
            v->y = v->y + amount;
            break;
        case 'E':
            v->x = v->x + amount;
            break;
        case 'W':
            v->x = v->x - amount;
            break;
    }
}

void moveForward(struct Vector *pos, struct Vector *waypoint, int amount) {
    printf("\nMoving ship... | %d, %d -> ", pos->x, pos->y);
    int x = waypoint->x, y = waypoint->y;
    multn(waypoint, amount);
    add(pos, waypoint);
    setPosition(waypoint, x, y, 0);
    printf("%d, %d\n", pos->x, pos->y);
}

void turn(struct Vector *v, char dir, int amount) {
    printf("\nTurning \e[0;32m%s\e[0m \e[0;35m%d\e[0m degrees... | Waypoint position: %d, %d -> ", dir == 'L' ? "LEFT" : "RIGHT", amount, v->x, v->y);
    int temp;
    switch (dir) {
        case 'L':
            rotate(v, 360 - amount);
            break;
        case 'R':
            rotate(v, amount);
            break;
    }
    printf("%d, %d\n", v->x, v->y);
}

void doAction(struct Vector *pos, struct Vector *waypoint, char action, int amount) {
    if (action == 'N' || action == 'S' || action == 'E' || action == 'W') {
        move(waypoint, action, amount);
    }
    else if (action == 'L' || action == 'R') {
        turn(waypoint, action, amount);
    }
    else {
        moveForward(pos, waypoint, amount);
    }
}

void parseInstructions(struct Vector *pos, struct Vector *waypoint, char **inst, int n) {
    for (int i = 0; i < n; i++) {
        char action = inst[i][0];
        int amount = atoi(copyFrom(inst[i], 0));

        doAction(pos, waypoint, action, amount);

    }
}

int manhattanDistance(struct Vector *v) {
    return abs(v->x) + abs(v->y);
}

int main(int argc, char **argv) {

    char **arr = readFile(argv[1]);
    int n = arrlen(arr);

    struct Vector pos;
    struct Vector waypoint;

    setPosition(&pos, 0, 0, 0);
    setPosition(&waypoint, 10, -1, 0);

    printf(SEP);

    parseInstructions(&pos, &waypoint, arr, n);

    printf("\n%s", SEP);

    int dist = manhattanDistance(&pos);

    printf("Manhattan distance to start: \e[0;36m%d\e[0m\n", dist);

    printf("%s\n", SEP);

    cleanMem(arr, MAX_LINES);

    return 0;
}