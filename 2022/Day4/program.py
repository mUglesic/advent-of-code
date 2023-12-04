
import sys

def solve(data):

    counter = 0

    for line in data:

        halfLine = line.split(',')

        elf1, elf2 = list(map(lambda x: int(x), halfLine[0].split('-'))), list(map(lambda x: int(x), halfLine[1].split('-')))

        # counter += (1 if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]) else 0)
        counter += (1 if not (elf1[1] < elf2[0] or elf1[0] > elf2[1]) else 0)

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