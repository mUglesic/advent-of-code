
import sys

pick_table = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

point_table = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

result_table = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"}
}

def solve(data):

    total = 0
    
    for line in data:
        
        picks = line.split(' ')
        
        total += pick_table[result_table[picks[0]][picks[1]]] + point_table[picks[1]]

    return total



def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    main()