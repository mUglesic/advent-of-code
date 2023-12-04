
import sys

def catchUp(head, tail):
    
    diff = Pos(head.x - tail.x, head.y - tail.y)

    if diff.x == 0:
        return Pos(tail.x, tail.y + (diff.y / abs(diff.y)))
    elif diff.y == 0:
        return Pos(tail.x + (diff.x / abs(diff.x)), tail.y)
    else:
        return Pos(tail.x + (diff.x / abs(diff.x)), tail.y + (diff.y / abs(diff.y)))

def solve(data):

    head = Pos(0, 0)
    tail = list(map(lambda x: Pos(0, 0), range(9)))

    posHistory = set()

    for line in data:

        direction, distance = line.split(' ')

        for i in range(int(distance)):

            match(direction):
                case 'U':
                    head = Pos(head.x, head.y - 1)
                case 'D':
                    head = Pos(head.x, head.y + 1)
                case 'L':
                    head = Pos(head.x - 1, head.y)
                case 'R':
                    head = Pos(head.x + 1, head.y)

            for j, piece in enumerate(tail):
                pieceAhead = head if j == 0 else tail[j - 1]
                if not pieceAhead.touching(piece):
                    tail[j] = catchUp(pieceAhead, piece)

            # print(head)
            
            posHistory.add(Pos(tail[-1].x, tail[-1].y))

    return len(posHistory)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def touching(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1
    def __str__(self):
        return f'{self.x, self.y}'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))


###########################

if __name__ == "__main__":
    main()