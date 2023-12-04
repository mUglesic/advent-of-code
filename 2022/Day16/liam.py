
import sys
import re

valves = {}

with open(sys.argv[1]) as f:

        for line in f:

            pattern = re.compile("Valve (?P<name>.*?) has flow rate=(?P<flow>.*?); tunnel(s?) lead(s?) to valve(s?) (?P<tunnels>.*?)$")

            match = pattern.match(line)

            name = match.group('name')
            flow = int(match.group('flow'))
            tunnels = match.group('tunnels').split(', ')

            # print(name, flow, tunnels)

            valves[name] = {'flow': flow, 'tunnels': tunnels, 'paths': {}}

keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

def bfs(frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1

for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

print(*[f'{x}: {valves[x]}' for x in valves], sep='\n')

def part1():

    best = 0

    def search(opened, flowed, current_room, depth_to_go):

        nonlocal best

        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k])

    search(set(['AA']), 0, 'AA', 29)

    return best

def part2():

    best = 0

    def search(opened, flowed, current_room, depth_to_go, elephants_turn):

        nonlocal best
        
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)

    search(set(['AA']), 0, 'AA', 25, False)
    
    return best

def main():

    # print(part1())

    # print(part2())

    pass


if __name__ == '__main__':
    main()