
import sys
import time

def findAntennas(data):

    antennas = {}

    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if el != '.':
                if el not in antennas:
                    antennas[el] = [(i, j)]
                else:
                    antennas[el].append((i, j))
    
    return antennas

def findNodes(antennas):

    nodes = set()

    for antenna, pos in antennas.items():
        for i in range(len(pos)):
            for j in range(i, len(pos)):
                p1, p2 = pos[i], pos[j]
                if p1 == p2: continue
                dist = (p1[0] - p2[0], p1[1] - p2[1])
                nodes.add((p1[0] + dist[0], p1[1] + dist[1]))
                nodes.add((p2[0] - dist[0], p2[1] - dist[1]))

    return nodes

def checkBounds(i, j, h, w):
    return i >= 0 and i < h and j >= 0 and j < w

def solve(data):

    nodes = findNodes(findAntennas(data))

    for node in nodes.copy():
        i, j = node
        if not checkBounds(i, j, len(data), len(data[0])):
            nodes.remove(node)

    return len(nodes)

def findNodesHarmonics(antennas, h, w):

    nodes = set()

    for antenna, pos in antennas.items():

        for i in range(len(pos)):
            for j in range(i, len(pos)):

                p1, p2 = pos[i], pos[j]
                nodes.add(p1)
                nodes.add(p2)

                if p1 == p2: continue

                dy, dx = p1[0] - p2[0], p1[1] - p2[1]

                y, x = p1[0], p1[1]

                while checkBounds(y + dy, x + dx, h, w):
                    nodes.add((y + dy, x + dx))
                    y += dy
                    x += dx

                y, x = p2[0], p2[1]
                    
                while checkBounds(y - dy, x - dx, h, w):
                    nodes.add((y - dy, x - dx))
                    y -= dy
                    x -= dx
                    
    return nodes

def solve2(data):

    nodes = findNodesHarmonics(findAntennas(data), len(data), len(data[0]))

    return len(nodes)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    #result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
