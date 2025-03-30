import math

PLAYER = 'O'  # 人間プレイヤー
AI = 'X'      # コンピュータ

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    win_states = [
        # 横
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # 縦
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # 斜め
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    return any(all(board[x][y] == player for x, y in line) for line in win_states)

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, PLAYER):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("三目並べスタート！あなたはO（先手）です")
    print_board(board)

    while True:
        # プレイヤーのターン
        while True:
            try:
                row = int(input("行 (0-2): "))
                col = int(input("列 (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = PLAYER
                    break
                else:
                    print("そのマスはすでに埋まっています。")
            except (ValueError, IndexError):
                print("0〜2の範囲で入力してください。")

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
