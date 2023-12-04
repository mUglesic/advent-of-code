
import sys
import re
import functools
import time

valves = {}

with open(sys.argv[1]) as f:

        for line in f:

            pattern = re.compile('Valve (?P<name>.*?) has flow rate=(?P<flow>.*?); tunnels? leads? to valves? (?P<tunnels>.*?)$')

            match = pattern.match(line)

            name = match.group('name')
            flow = int(match.group('flow'))
            tunnels = match.group('tunnels').split(', ')

            # print(name, flow, tunnels)

            valves[name] = {'flow': flow, 'tunnels': tunnels, 'paths': {}}

keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

def bfs(tunnels, end):

    depth = 1

    while True:

        nextTunnels = set()

        for tunnel in tunnels:
            if tunnel == end:
                return depth
            for nextTunnel in valves[tunnel]['tunnels']:
                nextTunnels.add(nextTunnel)

        tunnels = nextTunnels
        
        depth += 1

for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

# print(*[f'{x}: {valves[x]}' for x in valves], sep='\n')

@functools.cache
def searchOne(openedValves, currentValve, minutesLeft):

    best = 0

    if minutesLeft <= 0:
        return 0

    if currentValve not in openedValves:

        openedValves = set(openedValves)

        s = valves[currentValve]['flow'] * minutesLeft
        best = max(best, s + searchOne(frozenset(openedValves.union([currentValve])), currentValve, minutesLeft - 1))

    else:

        for nextValve in [valve for valve in valves[currentValve]['paths'].keys() if valve not in openedValves]:
            best = max(best, searchOne(openedValves, nextValve, minutesLeft - valves[currentValve]['paths'][nextValve]))

    # print(searchOne.cache_info())

    return best

@functools.cache
def searchTwo(openedValves, currentValve, minutesLeft, elephantTurn):

    best = 0

    if minutesLeft <= 0:
        return 0

    if currentValve not in openedValves:

        openedValves = set(openedValves)

        s = valves[currentValve]['flow'] * minutesLeft
        best = max(best, s + searchTwo(frozenset(openedValves.union([currentValve])), currentValve, minutesLeft - 1, elephantTurn))

        if not elephantTurn:
            # best = max(best, s + searchTwo(frozenset(set([currentValve]).union(openedValves)), 'AA', 25, True))
            best = max(best, s + searchTwo(frozenset(openedValves.union([currentValve])), 'AA', 25, True))

    else:

        for nextValve in [valve for valve in valves[currentValve]['paths'].keys() if valve not in openedValves]:
            best = max(best, searchTwo(openedValves, nextValve, minutesLeft - valves[currentValve]['paths'][nextValve], elephantTurn))

    return best

def main():

    # best = searchOne(frozenset(['AA']), 'AA', 29)
    best = searchTwo(frozenset(['AA']), 'AA', 25, False)

    print(best)


if __name__ == '__main__':
    startTime = time.time()
    main()
    print(f'Runtime: {time.time() - startTime} sec')