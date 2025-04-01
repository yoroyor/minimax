import math
import time

PLAYER = 'O'  # human
AI = 'X'      # AI
MAX_NUM = 5
MAX_DEPTH = 6

# dict for memoization
memo = {}

def board_to_tuple(board):
    """hash possible board state"""
    return tuple(tuple(row) for row in board)

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    win_states = [
        # 横
        [(0,0), (0,1), (0,2), (0,3), (0,4)],
        [(1,0), (1,1), (1,2), (1,3), (1,4)],
        [(2,0), (2,1), (2,2), (2,3), (2,4)],
        [(3,0), (3,1), (3,2), (3,3), (3,4)],
        [(4,0), (4,1), (4,2), (4,3), (4,4)],

        # 縦
        [(0,0), (1,0), (2,0), (3,0), (4,0)],
        [(0,1), (1,1), (2,1), (3,1), (4,1)],
        [(0,2), (1,2), (2,2), (3,2), (4,2)],
        [(0,3), (1,3), (2,3), (3,3), (4,3)],
        [(0,4), (1,4), (2,4), (3,4), (4,4)],
        # 斜め
        [(0,0), (1,1), (2,2), (3,3), (4,4)],
        [(0,4), (1,3), (2,2), (3,1), (4,0)]
    ]
    return any(all(board[x][y] == player for x, y in line) for line in win_states)

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def count_empty_cells(board):
    return sum(row.count(' ') for row in board)

# custom max depth based on the number of empty cells
# this is a simple heuristic to adjust the depth of the minimax algorithm
# based on the number of empty cells on the board
def create_custom_max_depth(board):
    empty_cells = count_empty_cells(board)
    if empty_cells > 20:
        return 0
    elif empty_cells > 18:
        return 2
    elif empty_cells > 12:
        return 5
    elif empty_cells > 10:
        return 10
    else:
        return 20
    

def minimax(board, depth, is_maximizing, alpha, beta, max_depth=5):
    
    if depth >= max_depth:
        return 0
    
    # this is a hash key for the current board state
    # to avoid recalculating the same state
    # in the minimax algorithm
    board_key = board_to_tuple(board)
    
    if board_key in memo:
        return memo[board_key]
    
    if check_winner(board, AI):
        return (20-depth)
    if check_winner(board, PLAYER):
        return (depth-20)
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(MAX_NUM):
            for j in range(MAX_NUM):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False, alpha, beta, max_depth)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
    else:
        best_score = math.inf
        for i in range(MAX_NUM):
            for j in range(MAX_NUM):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True, alpha, beta, max_depth)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
    
    # memoize the best score for the current board state
    # to avoid recalculating the same state
    # in the minimax algorithm
    memo[board_key] = best_score
    return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    
    max_depth = create_custom_max_depth(board)
    
    start_time = time.time()
    for i in range(MAX_NUM):
        for j in range(MAX_NUM):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, 0, False, -math.inf, math.inf, max_depth=max_depth)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
                    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"computer thinking time: {elapsed_time:.4f}s")
    return move

def main():
    board = [[' ' for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    print("game start")
    print_board(board)

    while True:
        while True:
            try:
                row = int(input("row (0-4): "))
                col = int(input("column (0-4): "))
                if board[row][col] == ' ':
                    board[row][col] = PLAYER
                    break
                else:
                    print("the cell is already occupied.")
            except (ValueError, IndexError):
                print("please enter a valid row and column (0-4).")

        print_board(board)

        if check_winner(board, PLAYER):
            print("you win!")
            break
        if is_full(board):
            print("withdraw.")
            break

        print("AI's turn")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI

        print_board(board)

        if check_winner(board, AI):
            print("AI win!")
            break
        if is_full(board):
            print("withdraw.")
            break

if __name__ == '__main__':
    main()
