
import sys
import time
import re

def solve(data):

    s = 0
    
    for line in data:

        [cardID, nums] = line.split(": ")

        cardID = cardID.split(" ")[-1]
        [winningNums, myNums] = nums.split(" | ")

        winningNums = re.sub(" +", " ", winningNums.strip()).split(" ")
        myNums = re.sub(" +", " ", myNums.strip()).split(" ")

        # print(cardID, winningNums, myNums, sep=" | ")

        worth = 0

        for num in myNums:
            if num in winningNums:
                worth = 1 if worth == 0 else worth * 2
        
        # print(cardID, " | ", worth)
        s += worth

    return s

def solve2(data):

    cardAmts = [1] * len(data)
    
    for line in data:

        [cardID, nums] = line.split(": ")

        cardID = int(cardID.split(" ")[-1])
        [winningNums, myNums] = nums.split(" | ")

        winningNums = re.sub(" +", " ", winningNums.strip()).split(" ")
        myNums = re.sub(" +", " ", myNums.strip()).split(" ")

        # print(cardID, winningNums, myNums, sep=" | ")

        matches = 0

        for num in myNums:
            if num in winningNums:
                matches += 1

        for i in range(matches):

            cardAmts[cardID + i] += cardAmts[cardID - 1]
        
        # print(cardID, " | ", worth)

    return sum(cardAmts)

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
