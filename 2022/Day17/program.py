
import sys
import time

# rockTypes = [
#     [
#         ['#', '#', '#', '#']
#     ],
#     [
#         ['.', '#', '.'],
#         ['#', '#', '#'],
#         ['.', '#', '.']
#     ],
#     [
#         ['.', '.', '#'],
#         ['.', '.', '#'],
#         ['#', '#', '#']
#     ],
#     [
#         ['#'],
#         ['#'],
#         ['#'],
#         ['#']
#     ],
#     [
#         ['#', '#'],
#         ['#', '#']
#     ]
# ]

rockTypes = [
    (2 + 3j, 3 + 3j, 4 + 3j, 5 + 3j),
    (2 + 4j, 3 + 3j, 3 + 4j, 3 + 5j, 4 + 4j),
    (2 + 3j, 3 + 3j, 4 + 3j, 4 + 34j, 4 + 5j),
    (2 + 3j, 2 + 4j, 2 + 5j, 2 + 6j),
    (2 + 3j, 2 + 4j, 3 + 3j, 3 + 4j)
]

ROCK_AMT = 2022
# ROCK_AMT = 1_000_000_000_000

def maxHeight():
    h = 0
    for i in range(ROCK_AMT):
        h += len(rockTypes[i % len(rockTypes)])
    return h

def setRock(chamber, rock):
    for i in range(rock.h):
        for j in range(rock.w):
            chamber[rock.y - i][rock.x + j] = rock.shape[i][j] if chamber[rock.y - i][rock.x + j] == '.' else chamber[rock.y - i][rock.x + j]

def solve(jetPattern):

    chamberHeight = maxHeight()
    chamberWidth = 7

    chamber = [['.' for x in range(chamberWidth)] for y in range(chamberHeight)]

    # print(*chamber[-5:], sep='\n')

    totalHeight = 0

    rockType = 0

    jetIndex = 0
    jetPatternSize = len(jetPattern)

    for i in range(ROCK_AMT):

        yStart = totalHeight + 2
        xStart = 2

        # print(xStart, yStart)

        rock = Rock(xStart, yStart, rockType)

        # print(rock)
        # print(*chamber[rock.y - rock.h:rock.y], sep='\n')

        while True:

            rock.shift(1 if jetPattern[jetIndex] == '>' else -1, chamber)

            jetIndex = (jetIndex + 1) % jetPatternSize

            dropped = rock.drop(-1, chamber)

            if not dropped:
                setRock(chamber, rock)
                break

        totalHeight = max(totalHeight, rock.y + 1)
        # print(totalHeight, rock.y + 1)

        rockType = (rockType + 1) % len(rockTypes)

        # print(*reversed(chamber[0:20]), sep='\n')
        # print()

    return totalHeight

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data[0])

    print(result)

class Rock:

    def __init__(self, x, y, type):
        
        self.shape = rockTypes[type]
        
        self.h = len(self.shape)
        self.w = len(self.shape[0])

        self.x = x
        self.y = y + self.h

    def shift(self, amt, chamber):

        # print(amt, self.x, self.x + self.w + amt)
        # print(*chamberSlice, sep='\n')
        
        if self.x + amt >= 0 and self.x + self.w + amt <= len(chamber[0]):

            colliding = False

            for i in range(self.h):
                for j in range(self.w):
                    if self.shape[i][j] == '#' and chamber[self.y - i][self.x + j + amt] == '#':
                        colliding = True
                        break
                if colliding: break
            
            if not colliding:
                self.x += amt
                return True

        return False
    
    def drop(self, amt, chamber):

        # print(self.y)
        # print(*chamberSlice, sep='\n')
        # print()
        
        if self.y + amt >= 0:

            colliding = False

            for i in range(self.h):
                for j in range(self.w):
                    if self.shape[i][j] == '#' and chamber[self.y - i + amt][self.x + j] == '#':
                        colliding = True
                        break
                if colliding: break

            if not colliding:
                self.y += amt
                return True

        # self.y += amt
        return False

    def __str__(self):
        return self.shape.__str__()


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
