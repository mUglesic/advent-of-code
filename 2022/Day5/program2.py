
import sys

def constrain(val, minVal, maxVal):
    return max(min(maxVal, val), minVal)

def parse(data, sep):

    stackCount = int(data[sep - 1][len(data[sep]) - 2])

    stacks = list(map(lambda x: [], range(0, stackCount)))

    for iLine, line in enumerate(data):

        if (iLine == sep - 1):
            break

        offset = 1

        for i in range(1, len(line), 4):
            
            crate = line[i]

            if crate != ' ':
                stacks[constrain(i - offset, 0, len(line))].append(crate)

            offset += 3

    return stacks

def solve(stacks, instructions):

    # print(stacks, instructions)

    for inst in instructions:

        vals = inst.split(' ')

        amt = int(vals[1])
        src = int(vals[3]) - 1
        end = int(vals[5]) - 1

        crates = []

        for i in range(0, amt):

            crate = stacks[src].pop(0)

            crates.append(crate)

        crates.extend(stacks[end])

        stacks[end] = crates

        # print(stacks)

    return ''.join(list(map(lambda stack: stack[0], stacks)))

def main():

    data = []

    sep = 0
    
    with open(sys.argv[1]) as f:

        i = 0

        for line in f:

            if (line == '\n'): sep = i

            data.append(line.strip('\n'))

            i += 1

    stacks = parse(data, sep)

    result = solve(stacks, data[sep + 1:])

    print(result)


###########################

if __name__ == "__main__":
    main()