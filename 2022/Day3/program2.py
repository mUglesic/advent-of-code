
import sys

def value(char):

    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1


def solve(data):

    total = 0

    for i in range(0, len(data), 3):
        
        backpacks = [data[i], data[i + 1], data[i + 2]]

        total += value(''.join(set(backpacks[0]).intersection(backpacks[1]).intersection(backpacks[2])))

    return total

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