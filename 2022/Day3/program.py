
import sys

def value(char):

    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1


def solve(data):

    total = 0

    for line in data:
        
        half1 = line[:len(line)//2]

        half2 = line[len(line)//2:]

        total += value(''.join(set(half1).intersection(half2)))

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