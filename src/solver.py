def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" |  ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row,colum

    return None


def valid(board, num, pos):
    # Check row for same number
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column for same number
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the box for same number

    box_pos_x = pos[1] // 3
    box_pos_y = pos[0] // 3

    for i in range(box_pos_y * 3, box_pos_y * 3 + 3):
        for j in range(box_pos_x * 3, box_pos_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    # If valid
    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Back Tracking Algorithm
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            # Recursively trying to find the solution with new board
            if solve(board):
                return True

            # When no match is found, then reset it to 0
            board[row][col] = 0

    return False
