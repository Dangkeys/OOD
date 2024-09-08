def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i] == j:
                return False
        
        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i] == j:
                return False
        
        return True

    def solve(board, row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1  # Backtrack

    result = []
    board = [-1] * n
    solve(board, 0)
    return result

def print_solution(solution):
    for board in solution:
        for i in board:
            print('. ' * i + 'Q ' + '. ' * (len(board) - i - 1))
        print()

n = 8
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solution(solutions)
