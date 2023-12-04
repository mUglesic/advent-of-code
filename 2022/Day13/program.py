
import sys
import ast

def checkOrder(p1, p2):

    p1len = len(p1)
    p2len = len(p2)

    for i in range(p1len):

        if p2len <= i: return False
        
        left = p1[i]
        right = p2[i]

        # print(left, right)

        if isinstance(left, int) and isinstance(right, int):

            if left < right: return True
            elif left > right: return False

        elif isinstance(left, list) and isinstance(right, list):

            sub = checkOrder(left, right)

            if sub is not None:
                return sub

        else:

            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right

            sub = checkOrder(left, right)

            if sub is not None:
                return sub

    if p1len < p2len: return True

    # return True



def solve(data):

    counter = 1
    sum = 0

    for i in range(0, len(data), 3):
        
        p1 = ast.literal_eval(data[i])
        p2 = ast.literal_eval(data[i + 1])

        # print(p1, p2)

        correct = checkOrder(p1, p2)

        # print(correct)

        if correct: sum += counter

        counter += 1

    return sum

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    main()