import sys

def main():

    values = []
    
    path = sys.argv[1]

    with open(path) as f:
        
        for line in f:
            
            values.append(int(line))

    print(solve1(values))

    print(solve2(values))

def solve1(values):
    
    count = 0

    for i in range(0, len(values) - 1):
        
        if values[i] < values[i + 1]:
            
            count += 1

    return count

def solve2(values):

    new_values = []

    for i in range(0, len(values) - 2):

        new_values.append(values[i] + values[i + 1] + values[i + 2])

    return solve1(new_values)

if __name__ == "__main__":
    main()