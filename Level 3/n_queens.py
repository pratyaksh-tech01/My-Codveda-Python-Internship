def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += "Q " if board[i][j] == 1 else ". "
        print(row)
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, row, i, n):
            board[row][i] = 1
            res = solve_nqueens(board, row + 1, n) or res
            board[row][i] = 0
    return res

if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens(board, 0, n):
        print("❌ No solution exists")
