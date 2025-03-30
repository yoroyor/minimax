import math
import time

PLAYER = 'O'  # 人間プレイヤー
AI = 'X'      # コンピュータ
MAX_NUM = 5
MAX_DEPTH = 6

# メモ化用の辞書
memo = {}

def board_to_tuple(board):
    """盤面をタプルに変換してハッシュ可能にする"""
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
    
    board_key = board_to_tuple(board)
    
    if board_key in memo:
        return memo[board_key]
    
    if check_winner(board, AI):
        return 1
    if check_winner(board, PLAYER):
        return -1
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
    print(f"コンピュータの思考時間: {elapsed_time:.4f}秒")
    return move

def main():
    board = [[' ' for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    print("五目並べスタート！あなたはO（先手）です")
    print_board(board)

    while True:
        # プレイヤーのターン
        while True:
            try:
                row = int(input("行 (0-4): "))
                col = int(input("列 (0-4): "))
                if board[row][col] == ' ':
                    board[row][col] = PLAYER
                    break
                else:
                    print("そのマスはすでに埋まっています。")
            except (ValueError, IndexError):
                print("0〜4の範囲で入力してください。")

        print_board(board)

        if check_winner(board, PLAYER):
            print("あなたの勝ち！")
            break
        if is_full(board):
            print("引き分けです。")
            break

        # コンピュータのターン
        print("コンピュータのターン...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI

        print_board(board)

        if check_winner(board, AI):
            print("コンピュータの勝ち！")
            break
        if is_full(board):
            print("引き分けです。")
            break

if __name__ == '__main__':
    main()
