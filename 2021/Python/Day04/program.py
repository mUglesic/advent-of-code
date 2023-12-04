
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

    marked_boards = [[[0 for el in line] for line in board] for board in boards]

    for num in nums:

        for b in range(len(boards)):
            for i in range(len(boards[b])):
                for j in range(len(boards[b][i])):

                    if boards[b][i][j] == num:

                        marked_boards[b][i][j] = 1

        # print(num)

        if (winning_board := game_over(marked_boards)) != -1:
            return calculate_sum(boards[winning_board], marked_boards[winning_board]) * num

def game_over(boards):

    for bi, board in enumerate(boards):

        # horizontal

        for line in board:

            if (all(el == 1 for el in line)):
                return bi

        # vertical

        for i in range(len(board)):

            temp = []

            for line in board:

                temp.append(line[i])

            if (all(el == 1 for el in temp)):
                return bi
    
    return -1

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

    print("Part One: {}".format(res))


if __name__ == "__main__":
    main()