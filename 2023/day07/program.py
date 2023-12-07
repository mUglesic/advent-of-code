
import sys
import time
from enum import Enum

# values = "AKQJT98765432"
values = "23456789TJQKA"
values2 = "J23456789TQKA"

class Types(Enum):

    HIGH = 1
    PAIR = 2
    TWOPAIR = 3
    THREE = 4
    FULL = 5
    FOUR = 6
    FIVE = 7

    def __lt__(self, other):
        return self.value < other.value

def solve(data):

    hands = []

    for line in data:

        hand, bid = line.split(" ")

        hands.append(Hand(hand, int(bid)))

    for hand in hands:
        hand.classify()

    hands.sort(key = lambda e : (e.type, [values.index(c) for c in e.hand]))

    s = 0

    for i, hand in enumerate(hands):
        s += (hand.bid * (i + 1))

    return s

def solve2(data):

    hands = []

    for line in data:

        hand, bid = line.split(" ")

        hands.append(Hand(hand, int(bid)))

    for hand in hands:

        if "J" in hand.hand:

            testHands = []

            for c in values2[1:]:
                testHands.append(Hand(hand.hand.replace("J", c), hand.bid))

            for h in testHands:
                h.classify()

            testHands.sort(key = lambda e : (e.type, [values2.index(c) for c in e.hand]))

            # print(testHands)

            hand.type = testHands[-1].type

        else:
            
            hand.classify()

    hands.sort(key = lambda e : (e.type, [values2.index(c) for c in e.hand]))

    # print(hands)

    s = 0

    for i, hand in enumerate(hands):
        s += (hand.bid * (i + 1))

    return s


def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

class Hand:

    cards = []
    hand = ""
    bid = 0
    type = Types.HIGH

    def __init__(self, cards, bid):
        self.cards = cards
        self.hand = "".join(self.cards)
        self.bid = bid

    def classify(self):
        count = {}

        for c in self.cards:
            try:
                count[c] += 1
            except:
                count[c] = 1

        twos = False
        twotwos = False
        threes = False
        fours = False
        fives = False

        for k, v in count.items():
            match(v):
                case 2:
                    if not twos:
                        twos = True
                    else:
                        twotwos = True
                case 3:
                    threes = True
                case 4:
                    fours = True
                case 5:
                    fives = True
        
        if fives:
            self.type = Types.FIVE
        elif fours:
            self.type = Types.FOUR
        elif twos and threes:
            self.type = Types.FULL
        elif twotwos:
            self.type = Types.TWOPAIR
        elif twos and not threes:
            self.type = Types.PAIR
        elif threes and not twos:
            self.type = Types.THREE
        else:
            self.type = Types.HIGH

        # self.type = count


    def __str__(self):
        return "(%s | %3d | %s)" % (self.cards, self.bid, self.type)
    
    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
