
import sys

def parse_data(data):

    drawn_nums = [int(i) for i in data[0].split(",")]
    boards = []

    bi = -1

    for i in range(2, len(data)):

        if (i + 5) % 6 == 0:
            continue

        if (i + 4) % 6 == 0:

            boards.append([])

            bi += 1

        boards[bi].append([int(l) for l in data[i].split()])

    return drawn_nums, boards

def solve(nums, boards):

    turns = [0 for b in boards]
    marked_boards = [[[0 for el in line] for line in board] for board in boards]

    for i, board in enumerate(boards):

        turns[i] = count_turns(nums, board, marked_boards[i])
    
    max_turns = max([(v, i) for i, v in enumerate(turns)])

    sum = calculate_sum(boards[max_turns[1]], marked_boards[max_turns[1]])

    return sum * nums[max_turns[0] - 1]

def count_turns(nums, board, marked):

    turns = 0

    while not won(marked):

        for i, line in enumerate(board):
            for j, el in enumerate(line):

                if el == nums[turns]:

                    marked[i][j] = 1
        
        turns += 1
    
    return turns

def won(board):

    # horizontal

    for line in board:

            if (all(el == 1 for el in line)): return True

    # vertical

    for i in range(len(board)):

        temp = []

        for line in board:

            temp.append(line[i])

        if (all(el == 1 for el in temp)): return True

def calculate_sum(board, marked):

    sum = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if marked[i][j] == 0:
                sum += board[i][j]

    return sum

def main():

    data = []

    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line)

    parsed_data = parse_data(data)

    drawn_nums = parsed_data[0]
    boards = parsed_data[1]

    res = solve(drawn_nums, boards)

    print("Part Two: {}".format(res))


if __name__ == "__main__":
    main()