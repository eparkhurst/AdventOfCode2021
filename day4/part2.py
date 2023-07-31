with open("input.txt") as f:
    input = f.read().strip().split("\n\n")

numbers = input[0].split(",")
boards = []
for board in input[1:]:
    arBoard = []
    for i, line in enumerate(board.split("\n")):
        arBoard.append(line.split())
    boards.append(arBoard)


def check_board(board):
    columns = [True] * len(board[0])
    for i, line in enumerate(board):
        row = True
        for j, char in enumerate(line):
            if char != "X":
                row = False
                columns[j] = False
        if row:
            return True
    if True in columns:
        return True
    return False


def count_board(board):
    count = 0
    for line in board:
        for char in line:
            if char != "X":
                count += int(char)
    return count


def get_loser():
    count = len(boards)
    for number in numbers:
        for b, board in enumerate(boards):
            if board == True:
                continue
            for i, line in enumerate(board):
                for j, char in enumerate(line):
                    if char == number:
                        board[i][j] = "X"
                        if check_board(board):
                            if count == 1:
                                return count_board(board) * int(number)
                            boards[b] = True
                            count -= 1


print(get_loser())
