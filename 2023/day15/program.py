
import sys
import time

def algo(s):

    val = 0

    for c in s:

        val += ord(c)
        val *= 17
        val = val % 256
    
    return val

def totalPower(boxes):

    power = 0

    for i, box in enumerate(boxes):

        if box:

            for j, (label, focalLength) in enumerate(box):

                power += ((1 + i) * (1 + j) * focalLength)

    return power

def solve(data):

    steps = data[0].split(",")

    s = 0

    for step in steps:

        s += algo(step)

    return s

def solve2(data):

    steps = data[0].split(",")

    boxes = []

    for _ in range(256):
        boxes.append([])

    for step in steps:

        # print(step)

        if "=" in step:

            l, fl = step.split("=")

            boxID = algo(l)
            found = False

            for i, (label, focalLength) in enumerate(boxes[boxID]):

                if label == l:
                    boxes[boxID][i] = (l, int(fl))
                    found = True
                    break
            
            if not found:
                boxes[boxID].append((l, int(fl)))

        elif "-" in step:

            boxID = algo(step[:-1])

            for label, focalLength in boxes[boxID]:

                if label == step[:-1]:
                    boxes[boxID].remove((label, focalLength))
        
        # print("After ", step, ":", sep="")
        # for i, box in enumerate(boxes):
        #     if box:
        #         print("Box ", i, ": ", sep="", end="")
        #         for label, focalLength in box:
        #             print("[", label, " ", focalLength, "]", sep="", end=" ")
        #         print()
        # print()
    
    return totalPower(boxes)

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
