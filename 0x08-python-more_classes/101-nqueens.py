#!/usr/bin/python3
"""a program that solves the N queens puzzle"""
import sys


def init_board(n):
    """initialise an N-by-N sized chessboard with zeros"""
    return [[0 for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col):
    """checks if placing a queen at (row, col) is safe"""
    for c in range(col):
        if board[row][c] == 1:
            return False
    for r in range(row):
        if board[r][col] == 1:
            return False

    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r = row + 1
    c = col + 1
    while r < len(board) and c < len(board):
        if board[r][c] == 1:
            return False
        r += 1
        c += 1

    r = row - 1
    c = col + 1
    while r >= 0 and c < len(board):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    r = row + 1
    c = col - 1
    while r < len(board) and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def solve_n_queens(board, row, solutions):
    """recursively solves the N-queens problem"""
    if row == len(board):
        solution = [i for i in range(len(board)) if board[i][i] == 1]
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1, solutions)
            board[row][col] = 0

    return (solutions)


def print_solution(solution):
    """prints a solution in the specified format (row indices)"""
    for col in solution:
        print(col + 1, end=" ")
    print()


def main():
    """program execution with input validation"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = solve_n_queens(board, 0, [])

    if solutions:
        print("Found solutions:")
        for sol in solutions:
            print_solution(sol)
    else:
        print("No solutions found for N-queens problem with size", n)


if __name__ == "__main__":
    main()
