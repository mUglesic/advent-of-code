
import sys

def solve(data):

    signal = data[0]

    counter = 0
    lastChars = []

    # distinct = 4
    distinct = 14

    for c in signal:

        # print(last4, len(last4) == 4 and len(last4) == len(set(last4)))

        if len(lastChars) == distinct and len(lastChars) == len(set(lastChars)):
            return counter
        elif len(lastChars) == distinct:
            lastChars.pop(0)
        
        lastChars.append(c)

        counter += 1

    return counter

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