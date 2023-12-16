
import sys
import time

def printDish(dish):

    for row in dish:
        for space in row:
            print(space, end="")
        print()
    print()

def tiltDish(dish, direction):

    dish = [list(row) for row in dish]

    match direction:

        case "north":

            for i in range(len(dish)):

                row = dish[i]

                for j, space in enumerate(row):

                    if space == "O":
                        
                        iNorth = i - 1

                        while iNorth >= 0 and dish[iNorth][j] not in "O#":

                            iNorth -= 1

                        row[j] = "."

                        dish[iNorth + 1][j] = "O"

        case "south":

            for i in range(len(dish) - 1, -1, -1):

                row = dish[i]

                for j, space in enumerate(row):

                    if space == "O":
                        
                        iSouth = i + 1

                        while iSouth < len(dish) and dish[iSouth][j] not in "O#":

                            iSouth += 1

                        row[j] = "."

                        dish[iSouth - 1][j] = "O"

        case "east":

            for i, row in enumerate(dish):
                for j in range(len(row) - 1, -1, -1):

                    space = row[j]

                    if space == "O":
                        
                        jEast = j + 1

                        while jEast < len(row) and dish[i][jEast] not in "O#":

                            jEast += 1

                        row[j] = "."

                        dish[i][jEast - 1] = "O"

        case "west":

            for i, row in enumerate(dish):
                for j in range(len(row)):

                    space = row[j]

                    if space == "O":
                        
                        jWest = j - 1

                        while jWest >= 0 and dish[i][jWest] not in "O#":

                            jWest -= 1

                        row[j] = "."

                        dish[i][jWest + 1] = "O"

    return tuple([tuple(row) for row in dish])

def spinCycle(dish):

    d = dish

    d = tiltDish(d, "north")
    d = tiltDish(d, "west")
    d = tiltDish(d, "south")
    d = tiltDish(d, "east")

    return d 

def totalLoad(dish):

    load = 0

    for i, row in enumerate(dish):
        for j, space in enumerate(row):

            if space == "O":

                load += len(dish) - i
    
    return load

def solve(data):

    tiltedDish = tiltDish(data, "north")

    return totalLoad(tiltedDish)

def solve2(data):

    dish = tuple([tuple(row) for row in data])

    seen = set(dish)
    history = [dish]

    # print([list(row) for row in dish])

    count = 0

    for i in range(1_000_000_000):

        count += 1
        
        dish = spinCycle(dish)

        # printDish(dish)
        # print(totalLoad(dish))

        if dish in seen:
            break

        seen.add(dish)
        history.append(dish)

    firstDish = history.index(dish)

    # printDish(dish)
    # printDish(history[firstDish])

    dish = history[(1_000_000_000 - firstDish) % (count - firstDish) + firstDish]

    # printDish(dish)

    return totalLoad(dish)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
