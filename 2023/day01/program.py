
txt2num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solve1():

    nums = []

    with open("example2.txt") as f:

        for line in f:

            d1 = ""
            d2 = ""

            for c in line:

                if c in "0123456789":
                    d1 = c if d1 == "" else d1

                    d2 = c

            nums.append(int(d1 + d2))

    print(sum(nums))

def solve2():

    nums = []

    with open("input") as f:

        for line in f:

            for subStr in txt2num:
                line = line.replace(subStr, subStr[0] + str(txt2num.index(subStr) + 1) + subStr[-1])

            d1 = ""
            d2 = ""

            for c in line:

                if c in "0123456789":
                    d1 = c if d1 == "" else d1

                    d2 = c

            nums.append(int(d1 + d2))

    print(sum(nums))


if __name__ == "__main__":
    # solve1()
    solve2()