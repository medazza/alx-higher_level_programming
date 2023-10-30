#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking 
queens on an N×N chessboard. 
Write a program that solves the N queens problem.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for ind in range(n)]
    [r.append(' ') for ind in range(n) for r in board]
    return (board)


def board_deepcopy(board):
    """Return a deep_copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return List of lists repres of a solved chessboard."""
    sol = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                sol.append([r, c])
                break
    return (sol)


def xout(board, rw, cl):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): Current working chessboard.
        row (int): Row where a queen was last played.
        col (int): Column where a queen was last played.
    """
    # X out all forward spots
    for c in range(cl + 1, len(board)):
        board[rw][c] = "x"
    # X out all backwards spots
    for c in range(cl - 1, -1, -1):
        board[rw][c] = "x"
    # X out all spots below
    for r in range(rw + 1, len(board)):
        board[r][cl] = "x"
    # X out all spots above
    for r in range(rw - 1, -1, -1):
        board[r][cl] = "x"
    # X out all spots diagonally down to the right
    c = cl + 1
    for r in range(rw + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = cl - 1
    for r in range(rw - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = cl + 1
    for r in range(rw - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = cl - 1
    for r in range(rw + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, sols):
    """Recursively solve An N-queens puzzle.
    Args:
        board (list): Current working chessboard.
        row (int): Current working row.
        queens (int): Current number of placed queens.
        solutions (list): List of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        sols.append(get_solution(board))
        return (sols)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            sols = recursive_solve(tmp_board, row + 1,
                                        queens + 1, sols)

    return (sols)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
