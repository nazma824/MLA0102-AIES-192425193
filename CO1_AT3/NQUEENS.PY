N = 12

board = [['.' for _ in range(N)] for _ in range(N)]

def is_safe(row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve(col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 'Q'

            if solve(col + 1):
                return True

            board[row][col] = '.'

    return False

if solve(0):
    print("12-Queens Solution:\n")

    for row in board:
        print(" ".join(row))

    print("\nTotal Queens Placed:", N)
else:
    print("No Solution Exists")
