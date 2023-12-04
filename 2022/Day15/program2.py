
import sys
import time
# from interval import interval, inf, imath
from multiprocessing import Pool

# MAX_SIZE = 20
MAX_SIZE = 4_000_000

def parseSensors(data):

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

    return sensors

def findGap(sensors, startRow, endRow):

    for row in range(startRow, endRow):

        # print(f'\nRow {row}:')

        i = Interval()

        for sensor in sensors:
            if sensor.y + sensor.d >= row >= sensor.y - sensor.d:
                off = abs(row - sensor.y)
                si = Interval(max(0, sensor.x - sensor.d + off), min(sensor.x + sensor.d - off, MAX_SIZE))
                i |= si
                # print(sensor, si)
        
        # print(f'Final interval for row {row}: ', i, '\n')

        if len(i) == 2:
            return (int(i[0].sup) + 1, row)


def solve(data):

    sensors = parseSensors(data)

    # Solo thread

    # return findGap(sensors, 0, MAX_SIZE)

    # Multiprocessing

    quarter = int(MAX_SIZE / 4)
    half = int(MAX_SIZE / 2)
    threeQuarters = int(3 * quarter)

    with Pool(4) as p:
        results = p.starmap(findGap, [(sensors, 0, quarter), (sensors, quarter, half), (sensors, half, threeQuarters), (sensors, threeQuarters, MAX_SIZE)])

    for result in results:
        if result: return result

    return (-1, -1)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    x, y = solve(data)

    print(x * 4_000_000 + y)

class Sensor:

    def __init__(self, x, y, closestBeacon):

        self.x = x
        self.y = y

        self.closestBeacon = closestBeacon
        self.d = self.dist(self.closestBeacon.x, self.closestBeacon.y)

    def dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)            

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

class Interval:

    def __init__(self, start = 0, end = 0):
        self.intervals = []
        if start != 0 or end != 0:
            self.intervals.append(SubInterval(start, end))

    def __len__(self):
        return len(self.intervals)

    def __or__(self, other):

        for oi in other.intervals:
            found = False
            for i in self.intervals:
                if i.intersects(oi):
                    i |= oi
                    found = True
            if not found:
                self.intervals.append(oi)
        
        self.intervals.sort(key=lambda x: x.inf)

        for i in range(len(self.intervals) - 1):
            try:
                left = self.intervals[i]
                right = self.intervals[i + 1]
                if left.intersects(right):
                    right |= left
                    self.intervals.pop(i)
                    i -= 1
            except:
                break

        return self

    def __getitem__(self, item):
        return self.intervals[item]

    def __str__(self):
        return 'Interval: [' + ', '.join(map(lambda x: x.__str__(), self.intervals)) + ']'

class SubInterval:

    def __init__(self, start, end):
        self.inf = start
        self.sup = end

    def intersects(self, other):
        return not (other.sup < self.inf or other.inf > self.sup)

    def __or__(self, other):
        self.inf = min(self.inf, other.inf)
        self.sup = max(self.sup, other.sup)
        return self

    def __str__(self):
        return f'[{self.inf}, {self.sup}]'


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print('Runtime: %s sec' % (time.time() - startTime))