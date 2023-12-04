
import sys

def parse_data(data):

    parsed = []

    for d in data:
        line = [p.strip().split(",") for p in d.split("->")]
        for point in line:
            for i in range(2): point[i] = int(point[i])
        parsed.append({"start": line[0], "end": line[1]})

    return parsed

def create_diagram(lines):

    max_x = -1; max_y = -1

    for line in lines:
        max_x = max(line["start"][0], line["end"][0], max_x)
        max_y = max(line["start"][1], line["end"][1], max_y)

    diagram = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

    return diagram

def fill_diagram(diagram, lines):

    for line in lines:

        if line["start"][0] == line["end"][0]:

            # print("Vertical:   {}".format(line))

            x = line["start"][0]

            y1 = line["start"][1]; y2 = line["end"][1]

            for y in range(y1, y2 + (1 if y2 > y1 else -1), 1 if y2 > y1 else -1):

                # print(x, y)

                diagram[y][x] += 1

        elif line["start"][1] == line["end"][1]:

            # print("Horizontal: {}".format(line))

            x1 = line["start"][0]; x2 = line["end"][0]

            y = line["start"][1]

            for x in range(x1, x2 + (1 if x2 > x1 else -1), 1 if x2 > x1 else -1):

                # print(x, y)

                diagram[y][x] += 1

        else:

            x1 = line["start"][0]; x2 = line["end"][0]
            y1 = line["start"][1]; y2 = line["end"][1]

            dist = abs(x2 - x1) + 1
            dir_x = 1 if x2 > x1 else -1
            dir_y = 1 if y2 > y1 else -1

            for i in range(dist):

                diagram[y1 + i * dir_y][x1 + i * dir_x] += 1

def count_overlaps(diagram):

    counter = 0

    for line in diagram:
        for el in line:
            if el >= 2: counter += 1

    return counter

def main():

    data = []

    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line)

    lines = parse_data(data)

    diagram = create_diagram(lines)

    fill_diagram(diagram, lines)

    # for i in diagram: print(i)

    res = count_overlaps(diagram)

    print("Overlaps: {}".format(res))

if __name__ == "__main__":
    main()