#include <iostream>
#include "../bugllib/lib.hpp"

const int CYCLES = 6;
const int BUFFER = 4;

int getIndex(int i, int j, int k, int l, int x, int y, int z) {
    return i * (x * y * z) + j * (x * y) + k * x + l;
}

void printDim(dataStructures::Array<char> dim, int x, int y, int z, int w) {
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < z; j++) {
            for (int k = 0; k < y; k++) {
                for (int l = 0; l < x; l++) {
                    std::cout << dim[getIndex(i, j, k, l, x, y, z)];
                }
                std::cout << "\n";
            }
            std::cout << "\n";
        }
    }
}

int countNeighbors(dataStructures::Array<char> dim, int i, int j, int k, int l, int x, int y, int z, int w) {
    int count = 0;

    for (int ii = i - 1; ii <= i + 1; ii++) {
        for (int jj = j - 1; jj <= j + 1; jj++) {
            for (int kk = k - 1; kk <= k + 1; kk++) {
                for (int ll = l - 1; ll <= l + 1; ll++) {
                    if (ii == i && jj == j && kk == k && ll == l) continue;
                    if(ii >= 0 && ii < w && jj >= 0 && jj < z && kk >= 0 && kk < y && ll >= 0 && ll < x) {
                        if (dim[getIndex(ii, jj, kk, ll, x, y, z)] == '#') count++;
                    }
                }
            }
        }
    }

    return count;
}

int countActive(dataStructures::Array<char> dim) {
    int count = 0;
    for (int i = 0; i < dim.length(); i++) {
        if (dim[i] == '#') count++;
    }
    return count;
}

int main(int argc, char **argv) {

    dataStructures::Array<std::string> arr = fileUtil::readFile(argv[1]);

    arr.print();

    int x = arr.length() + (CYCLES - 1) * 2 + BUFFER;
    int y = x;
    int z = CYCLES * 2 + 1 + BUFFER;
    int w = z;

    dataStructures::Array<char> dim(x * y * z * w);
    dim.fill('.');

    int startX = (CYCLES - 1) + 1;
    int startY = startX;
    int startZ = CYCLES + 1;
    int startW = startZ;

    for (int i = startY; i < startY + arr.length(); i++) {
        for (int j = startX; j < startX + arr.length(); j++) {
            dim[getIndex(startW, startZ, i, j, x, y, z)] = arr[i - startY][j - startX];
        }
    }

    // std::cout << "Starting dim:\n";
    // printDim(dim, x, y, z);
    // std::cout << "-------------\n";

    dataStructures::Array<char> copy = dim.copyOf();

    for (int c = 0; c < CYCLES; c++) {
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < z; j++) {
                for (int k = 0; k < y; k++) {
                    for (int l = 0; l < x; l++) {
                        int count = countNeighbors(copy, i, j, k, l, x, y, z, w);
                        int curIndex = getIndex(i, j, k, l, x, y, z);
                        if (copy[curIndex] == '#' && !(count == 2 || count == 3)) {
                            dim[curIndex] = '.';
                        }
                        else if (copy[curIndex] == '.' && count == 3) {
                            dim[curIndex] = '#';
                        }
                    }
                    //std::cout << "active neighbors for index: " << curIndex << ": " << count << "\n";
                }
            }
        }
        copy.clean();
        copy = dim.copyOf();
    }

    // printDim(dim, x, y, z);
    // std::cout << "----------\n";
    // printDim(copy, x, y, z);

    std::cout << "Active cubes: " << countActive(dim) << "\n";

    arr.clean();
    dim.clean();
    copy.clean();

    return 0;
}