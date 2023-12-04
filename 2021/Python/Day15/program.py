
import sys

def enlarge(data, factor):

    new_map = []

    for i in range(len(data) * factor):

        new_map.append([])

        for j in range(len(data) * factor):

            ii = int(i / len(data))
            jj = int(j / len(data))

            current_factor = ii + jj

            el = data[i % len(data)][j % len(data)] + current_factor

            new_map[i].append(el if el < 10 else (el % 10) + 1)
        
        # print("".join(map(str, new_map[i])))

    # for i in range(400, 500):
    #     for j in range(400, 500):
    #         print(new_map[i][j], end="")
    #     print()

    # print("".join(map(str, new_map[0:101])))

    # print(len(new_map))
    # print(new_map)

    return new_map

def find_lowest_risk(data):

    return risk_iter(data)

def risk_rec(x, y, data):

    if y >= len(data) or x >= len(data[y]):
        return sys.maxsize

    if y == len(data) - 1 and x == len(data[y]) - 1:
        return data[y][x]

    return data[y][x] + min(risk_rec(x + 1, y, data), risk_rec(x, y + 1, data))

def risk_iter(data):

    risk_table = [[0 for el in line] for line in data]

    for i in range(len(data)):
        for j in range(len(data[i])):

            if i == 0 and j == 0: continue

            risk_table[i][j] = data[i][j]

            if i == 0 and j > 0:
                risk_table[i][j] += risk_table[i][j - 1]

            elif i > 0 and j == 0:
                risk_table[i][j] += risk_table[i - 1][j]

            else:
                risk_table[i][j] += min(risk_table[i][j - 1], risk_table[i - 1][j])

        # print(" ".join(map(str, risk_table[i])))
        # print("Len: {} Line: {}".format(len(risk_table[i]), risk_table[i]))

    return risk_table[-1][-1]

def main():

    data = []

    with open(sys.argv[1]) as f:
        for line in f:
            data.append([int(el) for el in list(line.strip())])

    res1 = find_lowest_risk(data)
    res2 = find_lowest_risk(enlarge(data, 5))

    print("Part One: {}\nPart Two: {}".format(res1, res2))

if __name__ == "__main__":
    main()