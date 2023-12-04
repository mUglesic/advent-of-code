
import sys

# TARGET_ROW = 10
TARGET_ROW = 2_000_000

def solve(data):

    sensors = []
    beacons = set()

    for line in data:

        sensor, beacon = line.split(':')

        sensor = tuple(map(lambda x: int(x.split('=')[1]), sensor.split('at ')[1].split(', ')))
        beacon = tuple(map(lambda x: int(x.split('=')[1]), beacon.split('at ')[1].split(', ')))

        newBeacon = Beacon(beacon[0], beacon[1])
        newSensor = Sensor(sensor[0], sensor[1], newBeacon)

        beacons.add(newBeacon)
        sensors.append(newSensor)

    positions = set()

    for sensor in sensors:

        sensor.exclude(list(beacons))

        for element in sensor.poss:
            positions.add(element)

    return len(positions)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)

class Sensor:

    def __init__(self, x, y, closestBeacon):

        self.x = x
        self.y = y

        self.closestBeacon = closestBeacon
        self.d = self.dist(self.closestBeacon.x, self.closestBeacon.y)

        self.poss = self.getPositions(TARGET_ROW)

    def dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def getPositions(self, row):

        poss = []

        for x in range(self.x - self.d, self.x + self.d):
            if self.dist(x, row) <= self.d: poss.append((x, row))

        return poss

    def exclude(self, beacons):
        
        for beacon in beacons:
            try:
                i = self.poss.index(beacon.pos())
            except:
                pass
            else:
                self.poss.pop(i)
            

    def __str__(self):
        return f'sensor: {self.x}, {self.y}; closest beacon: {self.closestBeacon.x}, {self.closestBeacon.y}'

class Beacon:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'beacon: {self.x}, {self.y}'


###########################

if __name__ == "__main__":
    main()