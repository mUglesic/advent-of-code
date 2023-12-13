
import sys
import time

def printReflection(reflection):

    for row in reflection:

        print("".join(row))
        
    print()


def splitInput(data):

    reflections = []

    i = 0

    while i < len(data):

        reflection = []

        while i < len(data) and (row := data[i]):

            reflection.append(row)

            i += 1
        
        reflections.append(reflection)

        i += 1

    return reflections

def diff(a, b):

    count = 0

    for i in range(len(a)):
        count += 1 if a[i] != b[i] else 0

    return count

def possibleMirrors(reflection):

    # rows

    possibleRows = []

    for i in range(len(reflection) - 1):

        r1 = reflection[i]
        r2 = reflection[i + 1]

        if r1 == r2 or diff(r1, r2) == 1:
            possibleRows.append((i, i + 1))

    # cols

    possibleCols = []

    for i in range(len(reflection[0]) - 1):

        c1 = [row[i] for row in reflection]
        c2 = [row[i + 1] for row in reflection]

        if c1 == c2 or diff(c1, c2) == 1:
            possibleCols.append((i, i + 1))

    return possibleRows, possibleCols

def checkReflection(reflection, possibleRows, possibleCols):

    for up, down in possibleRows:

        start = up + 1
        mirrored = True
        fixedSmudge = False

        while up >= 0 and down < len(reflection):

            upRow = reflection[up]
            downRow = reflection[down]

            rowDiff = diff(upRow, downRow)

            if (rowDiff == 1 and fixedSmudge) or rowDiff > 1:
                mirrored = False
                break

            if rowDiff == 1 and not fixedSmudge:
                fixedSmudge = True

            up -= 1
            down += 1

        if mirrored and fixedSmudge:
            return start, "row"
    
    for left, right in possibleCols:

        start = left + 1
        mirrored = True
        fixedSmudge = False

        while left >= 0 and right < len(reflection[0]):

            leftCol = [row[left] for row in reflection]
            rightCol = [row[right] for row in reflection]

            colDiff = diff(leftCol, rightCol)

            if (colDiff == 1 and fixedSmudge) or colDiff > 1:
                mirrored = False
                break

            if colDiff == 1 and not fixedSmudge:
                fixedSmudge = True

            left -= 1
            right += 1
        
        if mirrored and fixedSmudge:
            return start, "col"

def reflectionScore(i, mirrorDirection):

    return i if mirrorDirection == "col" else i * 100

def solve(data):

    reflections = splitInput(data)

    totalScore = 0

    for reflection in reflections:

        possibleRows, possibleCols = possibleMirrors(reflection)

        # print(possibleRows, possibleCols)

        if len(possibleRows) == 1 and not possibleCols:
            totalScore += reflectionScore(possibleRows[0][0] + 1, "row")
        elif len(possibleCols) == 1 and not possibleRows:
            totalScore += reflectionScore(possibleCols[0][0] + 1, "col")
        else:
            totalScore += reflectionScore(*checkReflection(reflection, possibleRows, possibleCols))

    return totalScore

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
