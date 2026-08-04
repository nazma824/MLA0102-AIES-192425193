import math

ROWS = 6
COLS = 7

PLAYER = 'X'
AI = 'O'
EMPTY = '.'

board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print()
    for row in board:
        print(" ".join(row))
    print("0 1 2 3 4 5 6")
    print()


def is_valid(col):
    return board[0][col] == EMPTY


def get_next_row(col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None


def drop_piece(row, col, piece):
    board[row][col] = piece


def winning_move(piece):

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r][c + 1] == piece and
                board[r][c + 2] == piece and
                board[r][c + 3] == piece):
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and
                board[r + 1][c] == piece and
                board[r + 2][c] == piece and
                board[r + 3][c] == piece):
                return True

    # Positive Diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r + 1][c + 1] == piece and
                board[r + 2][c + 2] == piece and
                board[r + 3][c + 3] == piece):
                return True

    # Negative Diagonal
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r - 1][c + 1] == piece and
                board[r - 2][c + 2] == piece and
                board[r - 3][c + 3] == piece):
                return True

    return False


def board_full():
    for c in range(COLS):
        if board[0][c] == EMPTY:
            return False
    return True


def evaluate():

    if winning_move(AI):
        return 100

    if winning_move(PLAYER):
        return -100

    return 0


def minimax(depth, maximizing):

    score = evaluate()

    if depth == 0 or abs(score) == 100 or board_full():
        return score

    if maximizing:

        best = -math.inf

        for col in range(COLS):

            if is_valid(col):

                row = get_next_row(col)
                drop_piece(row, col, AI)

                value = minimax(depth - 1, False)

                board[row][col] = EMPTY

                best = max(best, value)

        return best

    else:

        best = math.inf

        for col in range(COLS):

            if is_valid(col):

                row = get_next_row(col)
                drop_piece(row, col, PLAYER)

                value = minimax(depth - 1, True)

                board[row][col] = EMPTY

                best = min(best, value)

        return best


def best_move():

    best_score = -math.inf
    move = None

    for col in range(COLS):

        if is_valid(col):

            row = get_next_row(col)
            drop_piece(row, col, AI)

            score = minimax(4, False)

            board[row][col] = EMPTY

            if score > best_score:
                best_score = score
                move = col

    return move


print("========== CONNECT FOUR AI ==========")
print("You are X")
print("AI is O")

while True:

    print_board()

    try:
        col = int(input("Enter column (0-6): "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if col < 0 or col >= COLS:
        print("Column must be between 0 and 6.")
        continue

    if not is_valid(col):
        print("Column is full.")
        continue

    row = get_next_row(col)
    drop_piece(row, col, PLAYER)

    if winning_move(PLAYER):
        print_board()
        print("Congratulations! You Win!")
        break

    if board_full():
        print_board()
        print("Game Draw!")
        break

    ai_col = best_move()

    if ai_col is not None:

        ai_row = get_next_row(ai_col)
        drop_piece(ai_row, ai_col, AI)

        print("AI chooses column:", ai_col)

        if winning_move(AI):
            print_board()
            print("AI Wins!")
            break

        if board_full():
            print_board()
            print("Game Draw!")
            break
