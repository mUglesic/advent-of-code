#include <iostream>
#include <string>

#include "../bugllib/lib.hpp"
// #include "../bugllib/color.hpp"
// #include "../bugllib/emoji.hpp"

int doOp(int left, char op, int right) {
    switch (op) {
        case '+':
            return left + right;
        case '*':
            return left * right;
        default:
            return -1;
    }
}

int solve(dataStructures::Array<std::string> eq) {

    eq.print();

    int result = std::stoi(eq[0]);

    for (int i = 0; i < eq.length() - 1; i += 2) {
        // std::cout << "length: " << eq.length() << " index: " << i << "\n";
        char op = eq[i + 1][0];
        int right = std::stoi(eq[i + 2]);

        std::cout << "operation: " << result << op << right;

        result = doOp(result, op, right);

        std::cout << " = " << result << "\n";

    }

    return result;
}

int main(int argc, char **argv) {

    dataStructures::Array<std::string> arr = fileUtil::readFile(argv[1]);

    int sum = 0;

    for (int i = 0; i < arr.length(); i++) {

        int result = solve(stringUtil::split(arr[i], ' '));

        std::cout << arr[i] << ": " << result << "\n";

        sum += result;

    }

    std::cout << sum << "\n";

    arr.clean();

    return 0;
}