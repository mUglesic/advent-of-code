
import sys

def solve_first(data, steps):

    s = 0

    for i in range(steps):

        increment_all(data)

        s += flash(data)

        reset_flashed(data)

    return s

def solve_second(data):

    done = False

    counter = 0

    while not done:

        increment_all(data)

        flash(data)

        done = all_flashed(data)

        reset_flashed(data)

        counter += 1

    return counter

def increment_all(data):

    for line in data:
        for el in line:
            el.increment()

def flash(data):

    count = 0

    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if el.energy > 9 and not el.flashed:
                count += flash_rec(i, j, data)

    return count

def flash_rec(i, j, data):

    oct = data[i][j]

    if oct.flashed or oct.energy < 10:
        return 0

    oct.flash()

    s = 1

    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):

            # print(ii, jj)

            if ii < 0 or ii > len(data) - 1 or jj < 0 or jj > len(data[ii]) - 1: continue

            neighbor = data[ii][jj]

            neighbor.increment()

            s += flash_rec(ii, jj, data)

    return s

def all_flashed(data):

    done = True

    for line in data:
        for el in line:
            if not el.flashed:
                done = False

    return done

def reset_flashed(data):

    for line in data:
        for el in line:
            if el.flashed: el.reset()

def main():

    data = []

    with open(sys.argv[1]) as f:
        for line in f:
            data.append([int(el) for el in list(line.strip())])

    oct1 = [[Octopus(el) for el in line] for line in data]
    oct2 = [[Octopus(el) for el in line] for line in data]

    res1 = solve_first(oct1, 100)
    res2 = solve_second(oct2)

    print("Part One: {}\nPart Two: {}".format(res1, res2))

########################################################################

class Octopus:

    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def increment(self):
        self.energy += 1

    def flash(self):
        self.flashed = True

    def reset(self):
        self.flashed = False
        self.energy = 0

    def __str__(self):
        return "{}".format(self.energy)

if __name__ == "__main__":
    main()