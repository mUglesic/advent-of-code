
import sys
import re
import functools

valves = {}

def parseValves(data):

    valves = {}

    for line in data:

        pattern = re.compile("Valve (?P<name>.*?) has flow rate=(?P<flow>.*?); tunnel(s?) lead(s?) to valve(s?) (?P<tunnels>.*?)$")

        match = pattern.match(line)

        name = match.group('name')
        flow = int(match.group('flow'))
        tunnels = match.group('tunnels').split(', ')

        # print(name, flow, tunnels)

        valves[name] = {'flowRate': flow, 'valves': tunnels}

        # valves.append(Valve(name, flow))

    # for i, line in enumerate(data):

    #     v = line.split('; ')[1]

    #     pattern = re.compile("tunnel(s?) lead(s?) to valve(s?) (?P<tunnels>.*?)$")

    #     match = pattern.match(v)

    #     tunnels = match.group('tunnels').split(', ')

    #     for tunnel in tunnels:
    #         valves[i].connect(findValve(valves, tunnel))

    return valves

def findValve(valves, name):
    for valve in valves:
        if valve.name == name:
            return valve

def openValveFlow(valves):
    return sum([v.flowRate for v in valves])

def allOpen(valves, openValves):
    for valve in valves:
        if valve.flowRate > 0 and valve not in openValves:
            return False
    return True

def maxFlow(currentValve, minute, totalFlow, valves, openValves):

    print(*openValves, sep=', ')

    if allOpen(valves, openValves):
        totalFlow += (openValveFlow(openValves) * (30 - minute))
        # print(minute, currentValve.name, openValveFlow(openValves), totalFlow)
        return totalFlow

    if minute >= 30:
        return totalFlow

    if currentValve.flowRate == 0 or currentValve in openValves:
        return max([maxFlow(v, minute + 1, totalFlow + openValveFlow(openValves), valves, openValves) for v in currentValve.connected])

    closed = max([maxFlow(v, minute + 1, totalFlow + openValveFlow(openValves), valves, openValves) for v in currentValve.connected])

    minute += 1
    totalFlow += openValveFlow(openValves)
    # currentValve.open()
    openValves.add(currentValve)

    opened = max([maxFlow(v, minute + 1, totalFlow + openValveFlow(openValves), valves, openValves) for v in currentValve.connected])

    return max(closed, opened)

@functools.cache
def one(currentValve, minutesLeft, openValves):

    if minutesLeft <= 0:
        return 0

    # print(minutesLeft)
    
    bestRes = 0

    current = valves[currentValve]

    for valve in current['valves']:
        bestRes = max(bestRes, one(valve, minutesLeft - 1, openValves))

    if currentValve not in openValves and current['flowRate'] > 0 and minutesLeft > 0:

        openValves = set(openValves)
        openValves.add(currentValve)
        minutesLeft -= 1
        s = minutesLeft * current['flowRate']

        for valve in current['valves']:
            bestRes = max(bestRes, s + one(valve, minutesLeft - 1, frozenset(openValves)))

    return bestRes

@functools.cache
def two(currentValve, minutesLeft, openValves):

    if minutesLeft <= 0:
        return one('AA', 26, openValves)

    # print(minutesLeft)
    
    bestRes = 0

    current = valves[currentValve]

    for valve in current['valves']:
        bestRes = max(bestRes, two(valve, minutesLeft - 1, openValves))

    if currentValve not in openValves and current['flowRate'] > 0 and minutesLeft > 0:

        openValves = set(openValves)
        openValves.add(currentValve)
        minutesLeft -= 1
        s = minutesLeft * current['flowRate']

        for valve in current['valves']:
            bestRes = max(bestRes, s + two(valve, minutesLeft - 1, frozenset(openValves)))

    return bestRes

def solve(data):

    global valves
    valves = parseValves(data)

    # return one('AA', 30, frozenset())
    return two('AA', 26, frozenset())

    # return maxFlow(valves[0], 1, 0, valves, set())

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)

class Valve:

    def __init__(self, name, flow):

        self.name = name
        self.flowRate = flow

        self.isOpen = False

        self.connected = []

    def connect(self, other):
        self.connected.append(other)

    def open(self):
        self.isOpen = True

    def __str__(self):
        return f'Valve {self.name} | Flow rate: {self.flowRate} | Tunnels: {", ".join(map(lambda x: x.name, self.connected))}'


###########################

if __name__ == "__main__":
    main()