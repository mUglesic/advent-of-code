
import sys
import time

def isOrdered(page, rules):

    for i, num in enumerate(page):

        if num not in rules:
            continue

        numRules = rules[num]

        for checkNum in page[0:i]:
            if checkNum in numRules:
                return False
        
    return True

def solve(data):

    rules = {}

    while (line := data.pop(0)) != "":
        
        x, y = line.split("|")

        if x not in rules:
            rules[x] = {y}
        else:
            rules[x].add(y)

    ordered = []

    for line in data:
        
        page = line.split(",")

        if isOrdered(page, rules):
            ordered.append([int(n) for n in page])

    sum = 0

    for l in ordered:
        sum += l[int((len(l) - 1) / 2)]

    return sum

def order(page, rules):
    
    while not isOrdered(page, rules):

        for i, el1 in enumerate(page):

            if el1 not in rules: continue

            for j, el2 in enumerate(page[0:i]):

                if el2 in rules[el1]:
                    # print(f"swapping {el1} <--> {el2}")
                    page[i], page[j] = page[j], page[i]

    return page

def solve2(data):

    rules = {}

    while (line := data.pop(0)) != "":
        
        x, y = line.split("|")

        if x not in rules:
            rules[x] = {y}
        else:
            rules[x].add(y)

    incorrect = []

    for line in data:
        
        page = line.split(",")

        if not isOrdered(page, rules):
            incorrect.append(page)

    ordered = []

    for page in incorrect:

        ordered.append([int(n) for n in order(page, rules)])

    sum = 0

    for l in ordered:
        sum += l[int((len(l) - 1) / 2)]

    return sum

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
