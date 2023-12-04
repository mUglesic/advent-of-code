
import sys

mod = 1

def parse(data):

    monkeys = []

    for i in range(0, len(data), 7):

        number = data[i].split(' ')[1][:-1]
        items = list(map(lambda x: Item(int(x)), data[i + 1].split(': ')[1].split(', ')))
        operation = data[i + 2].split('= ')[1].split(' ')
        test = int(data[i + 3].split('by ')[1])
        testT = int(data[i + 4].split('monkey ')[1])
        testF = int(data[i + 5].split('monkey ')[1])

        monkeys.append(Monkey(number, items, Operation(operation[0], operation[1], operation[2]), Test(test, testT, testF)))

    return monkeys

def solve(data):

    monkeys = parse(data)

    # rounds = 20
    rounds = 10_000

    global mod

    for monkey in monkeys:
        mod *= monkey.test.div

    for round in range(rounds):

        for monkey in monkeys:

            while monkey.items:

                inspectionResult = monkey.inspect()

                monkeys[inspectionResult["target"]].add(inspectionResult["item"])

        # print(round)

    monkeys.sort(reverse=True, key=lambda m: m.itemsInspected)

    print(list(map(lambda m: f'Monkey {m.number}: {str(m)}', monkeys)))

    return monkeys[0].itemsInspected * monkeys[1].itemsInspected

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)

class Item:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'{self.val}'

class Monkey:

    def __init__(self, number, startingItems, operation, test):
        self.number = number
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.itemsInspected = 0

    def inspect(self):

        self.itemsInspected += 1

        item = self.items.pop(0)

        item.val = self.operation.do(item.val)
        # item.val = int(math.floor(item.val / 3))
        # item.val = item.val % self.test.div
        item.val = item.val % mod

        return {"item": item, "target": self.test.test(item.val)}

    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return '[' + ', '.join(map(lambda i: str(i.val), self.items)) + f'] | Items inspected: {self.itemsInspected}'

class Operation:

    def __init__(self, first, op, second):
        self.first = first
        self.op = op
        self.second = second

    def do(self, val):

        left = int(self.first) if self.first != 'old' else val
        right = int(self.second) if self.second != 'old' else val

        match (self.op):
            case '*':
                return left * right
            case '+':
                return left + right

class Test:

    def __init__(self, div, t, f):
        self.div = div
        self.t = t
        self.f = f

    def test(self, val):
        return self.t if val % self.div == 0 else self.f

###########################

if __name__ == "__main__":
    main()