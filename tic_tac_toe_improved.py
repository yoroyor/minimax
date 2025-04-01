import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def empty_spots(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def minimax(board, depth, is_maximizing, original_player):
    opponent = 'O' if original_player == 'X' else 'X'
    winner = check_winner(board)

    if winner or not empty_spots(board):
        if winner == original_player:
            return (10 - depth, None)
        elif winner == opponent:
            return (depth - 10, None)
        else:
            return (0, None)

    current_player = original_player if is_maximizing else opponent
    best_move = None

    if is_maximizing:
        best_score = float('-inf')
        for i, j in empty_spots(board):
            board[i][j] = current_player
            score, _ = minimax(board, depth + 1, False, original_player)
            board[i][j] = ' '
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float('inf')
        for i, j in empty_spots(board):
            board[i][j] = current_player
            score, _ = minimax(board, depth + 1, True, original_player)
            board[i][j] = ' '
            if score < best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move

def main():
    if len(sys.argv) != 5:
        print("Usage: python tic_tac_toe_improved.py 'row1' 'row2' 'row3' player")
        sys.exit(1)

    board = [list(sys.argv[1]), list(sys.argv[2]), list(sys.argv[3])]
    player = sys.argv[4].upper()

    if player not in ['X', 'O']:
        print("Error: Player must be 'X' or 'O'.")
        sys.exit(1)

    print("Initial board:")
    print_board(board)

    _, move = minimax(board, 0, player == 'O', player)

    if move:
        i, j = move
        board[i][j] = player
        print(f"Best move: ({i}, {j})")
        print("Updated board after the move:")
        print_board(board)
    else:
        print("No valid moves available. Game might be over.")
        print_board(board)

if __name__ == "__main__":
    main()