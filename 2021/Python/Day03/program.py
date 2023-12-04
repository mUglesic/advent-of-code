import sys

def bin_dec(bn):
    dn = 0

    for i, c in enumerate(reversed(bn)):
        dn += (int(c) * pow(2, i))
    
    return dn

def count_ones(data):

    counter = []

    for i in range(0, len(data[0])):
        counter.append(0)

    for num in data:

        for i, c in enumerate(num):

            if c == "1":

                counter[i] += 1
    
    return counter

def solve1(data, counter):

    gamma = ""
    epsilon = ""

    for val in counter:

        if val > len(data) / 2:

            gamma += "1"
            epsilon += "0"
        
        else:

            gamma += "0"
            epsilon += "1"

    gamma_dec = bin_dec(gamma)
    epsilon_dec = bin_dec(epsilon)

    return gamma_dec * epsilon_dec

def solve2(data, counter):

    oxy = solve2_rec(data, counter, 0, "1")
    co2 = solve2_rec(data, counter, 0, "0")

    oxy_dec = bin_dec(oxy)
    co2_dec = bin_dec(co2)

    return oxy_dec * co2_dec

def solve2_rec(candidates, counter, index, criteria):

    if len(candidates) == 1:
        return candidates[0]

    inverse_criteria = "0" if criteria == "1" else "1"

    new_candidates = []

    for c in candidates:

        if counter[index] >= len(candidates) / 2:

            if c[index] == criteria:

                new_candidates.append(c)
        
        else:

            if c[index] == inverse_criteria:

                new_candidates.append(c)

    #print(index, new_candidates)

    new_counter = count_ones(new_candidates)

    return solve2_rec(new_candidates, new_counter, index + 1, criteria)


def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    counter = count_ones(data)

    res1 = solve1(data, counter)
    res2 = solve2(data, counter)

    print("Part One: {}\nPart Two: {}".format(res1, res2))

if __name__ == "__main__":
    main()