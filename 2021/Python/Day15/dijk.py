
import sys
import heapq
from heapdict import heapdict
import time

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
        
    return new_map

def dijk(data):

    q = []

    n = []

    h = []

    for i, line in enumerate(data):
        n.append([])
        for j, el in enumerate(line):
            # print(i, j)
            new_node = Node(i, j, el)
            n[i].append(new_node)
            q.append(new_node)

    q[0].d = 0
    q[0].total_d = 0

    target = q[-1]

    heapq.heappush(h, q[0])

    for node in q:
        node.add_neighbors(n)

    # print(q[0].neighbors)

    print("finished adding neighbors")

    while len(h) > 0:

        u = heapq.heappop(h)

        # print(len(h))

        if u == target:
            print(u, target)
            return u

        for v in u.neighbors:

            alt = u.total_d + v.d

            if alt < v.total_d:
                v.total_d = alt
                v.prev = u
                heapq.heappush(h, v)

    return target

def dijk2(data):

    q = heapdict()

    n = []

    target = None

    for i, line in enumerate(data):
        n.append([])
        for j, el in enumerate(line):
            # print(i, j)
            new_node = Node(i, j, el)
            if i == 0 and j == 0:
                new_node.d = 0
                new_node.total_d = 0
            if i == len(data) - 1 and j == len(line) - 1:
                target = new_node
            n[i].append(new_node)
            q[new_node] = new_node.total_d

    for node in q:
        node.add_neighbors(n)

    print("finished adding neighbors")

    while len(q) > 0:
        
        (u, p) = q.popitem()

        if u == target:
            print(u, target)
            return u

        for v in u.neighbors:

            alt = u.total_d + v.d

            if alt < v.total_d:
                v.total_d = alt
                v.prev = u
                q[v] = alt

    return target

def find_node(arr, i, j):

    for node in arr:
        if node.i == i and node.j == j:
            return node
    
    return None

def find_min_dist(arr):

    lowest = 0

    for i, node in enumerate(arr):
        if node.total_d < arr[lowest].total_d:
            lowest = i

    return arr[lowest]

def main():

    data = []

    with open(sys.argv[1]) as f:
        for line in f:
            data.append([int(el) for el in list(line.strip())])

    start_time = time.time()
    # res1 = dijk(data)
    res2 = dijk(enlarge(data, 5))
    end_time = time.time()

    print(end_time - start_time)

    # print(res1)
    print(res2)

    # print("Part One: {}\nPart Two: {}".format(res1, res2))

######################################################

class Node:

    def __init__(self, i, j, d):
        
        self.i = i
        self.j = j
        self.d = d

        self.total_d = sys.maxsize
        self.prev = None

        self.neighbors = []

    def add_neighbors(self, grid):

        i = self.i
        j = self.j

        if (i > 0):
            self.neighbors.append(grid[i - 1][j])
        if (i < len(grid) - 1):
            self.neighbors.append(grid[i + 1][j])
        if (j > 0):
            self.neighbors.append(grid[i][j - 1])
        if (j < len(grid[i]) - 1):
            self.neighbors.append(grid[i][j + 1])

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __lt__(self, other):
        return self.total_d < other.total_d
    
    def __hash__(self):
        return hash((self.i, self.j))

    def __str__(self):
        return "i: {}, j: {}, Distance: {}".format(self.i, self.j, self.total_d)

if __name__ == "__main__":
    main()