
import sys
import time

def solve(data):

    cubes = []
    sides = {}

    for line in data:

        cube = tuple(int(x) for x in line.split(','))

        cubes.append(cube)
        sides[cube] = 6

    for x1,y1,z1 in cubes:
        for x2,y2,z2 in cubes:
            
            if x1 == x2 and y1 == y2 and z1 == z2:
                continue

            if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1:
                sides[(x1,y1,z1)] -= 1

    return sum(sides.values())

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
