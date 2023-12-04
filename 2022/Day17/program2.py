
import sys
import time
from itertools import cycle

rockTypes = [
    (2 + 3j, 3 + 3j, 4 + 3j, 5 + 3j),
    (2 + 4j, 3 + 3j, 3 + 4j, 3 + 5j, 4 + 4j),
    (2 + 3j, 3 + 3j, 4 + 3j, 4 + 4j, 4 + 5j),
    (2 + 3j, 2 + 4j, 2 + 5j, 2 + 6j),
    (2 + 3j, 2 + 4j, 3 + 3j, 3 + 4j)
]

ROCK_AMT_ONE = 2022
# ROCK_AMT_TWO = 1_000_000_000_000
ROCK_AMT_TWO = 1000000000000

N_ROWS = 30

# def unique(chamber, height):
#     return frozenset([(r - (height - r.imag) * 1j) for r in chamber if height - r.imag <= N_ROWS])

def mapNRocks(jetPattern, nRocks):

    jetPattern = [1 if j == '>' else -1 for j in jetPattern]

    chamberWidth = 7
    chamber = set( i - 1j for i in range(chamberWidth) )

    totalHeight = 0

    rockCycle = cycle(enumerate(rockTypes))
    jetCycle = cycle(enumerate(jetPattern))

    heightAfterRock = {}
    repeats = []

    for i, (iRock, rock) in zip(range(1, nRocks + 1), rockCycle):

        # Create the rock shifted up by tower height

        rock = tuple( r + totalHeight * 1j for r in rock )

        while True:

            # Get shift direction

            iJet, jet = next(jetCycle)

            # Attempt to shift the rock

            newRock = tuple( r + jet for r in rock )

            # Check collisions for new position

            if all( 0 <= r.real < chamberWidth for r in newRock ) and not chamber & set(newRock):
                # Confirm the shift
                rock = newRock

            # Attempt to drop the rock by one

            newRock = tuple( r - 1j for r in rock )

            # Check collisions for new position

            if chamber & set(newRock):

                # Hit

                chamber.update(rock)
                totalHeight = max(totalHeight, *( int(r.imag) + 1 for r in rock ))

                if i % len(rockTypes) == 0 and iJet == 0:
                    repeats.append((i, totalHeight))
                    print(f'Rock: {i} | Height: {totalHeight}')

                break

            else:
                # Confirm the drop
                rock = newRock

                if i % len(rockTypes) == 0 and iJet == 0:
                    repeats.append((i, totalHeight))
                    print(f'Rock: {i} | Height: {totalHeight}')

        heightAfterRock[i] = totalHeight

    # with open('rockMap2022.txt', 'w', newline='\n') as f:
    #     for i in range(totalHeight, -1, -1):
    #         for j in range(chamberWidth):
    #             f.write('.#'[j + i * 1j in chamber])
    #         f.write('\n')

    return (repeats, heightAfterRock)

def partTwo(repeats, rockMap):

    startRepeat, h1 = repeats[1]
    endRepeat, h2 = repeats[2]

    rockStep = endRepeat - startRepeat
    heightStep = h2 - h1

    reps = ROCK_AMT_TWO // rockStep
    repHeight = reps * heightStep

    endBit = ROCK_AMT_TWO - (reps * rockStep)

    return repHeight + rockMap[endBit]

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    repeats, rockMap = mapNRocks(data[0], 5 * 10091 + 1)
    # chamber, rockMap = mapNRocks(data[0], 10_091)

    print(f'Height after [{ROCK_AMT_ONE}] rocks: {rockMap[ROCK_AMT_ONE]}')

    print(f'Height after [{ROCK_AMT_TWO}] rocks: {partTwo(repeats, rockMap)}')

###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
