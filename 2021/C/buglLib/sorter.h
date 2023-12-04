
int intComp(const void *el1, const void *el2) {
    int f = *((int *) el1);
    int s = *((int *) el2);
    return (f > s) - (f < s);
}