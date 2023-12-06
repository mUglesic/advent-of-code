
import sys
import time
import re

def simulateRace(t, d):

    wins = 0

    for timeHeld in range(t):

        dist = (t - timeHeld) * timeHeld

        wins += 1 if dist > d else 0

    return wins

def solve(data):

    times = re.sub(" +", " ", data[0].split(":")[1].strip()).split(" ")
    distance = re.sub(" +", " ", data[1].split(":")[1].strip()).split(" ")

    totalScore = 1

    for i in range(len(times)):

        t = int(times[i])
        d = int(distance[i])

        totalScore *= simulateRace(t, d)

    return totalScore

def solve2(data):

    t = int(data[0].split(":")[1].replace(" ", ""))
    d = int(data[1].split(":")[1].replace(" ", ""))

    return simulateRace(t, d)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
