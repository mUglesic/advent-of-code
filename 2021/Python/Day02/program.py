import sys

def main():

    values = []
    
    path = sys.argv[1]

    with open(path) as f:
        
        for line in f:
            
            split_line = line.split(" ")

            values.append({"command": split_line[0], "value": int(split_line[1])})

    print(solve1(values))

    print(solve2(values))

def solve1(values):

    pos = 0
    depth = 0

    for cmd in values:

        match cmd["command"]:
            case "forward":
                pos += cmd["value"]
            case "down":
                depth += cmd["value"]
            case "up":
                depth -= cmd["value"]

    print("Part One | Position: {} | Depth: {}".format(pos, depth))

    return pos * depth

def solve2(values):

    pos = 0
    depth = 0
    aim = 0

    for cmd in values:

        match cmd["command"]:
            case "down":
                aim += cmd["value"]
            case "up":
                aim -= cmd["value"]
            case "forward":
                pos += cmd["value"]
                depth += (aim * cmd["value"])

    print("Part Two | Position: {} | Depth: {}".format(pos, depth))

    return pos * depth

if __name__ == "__main__":
    main()