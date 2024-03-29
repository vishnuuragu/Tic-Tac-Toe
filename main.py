import tkinter as tk
from tkinter import messagebox

def click(row, col):
    if board[row][col] == " " and not check_win(board):
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        if not check_win(board):
            computer_move(board)
            if check_win(board):
                messagebox.showinfo("Tic Tac Toe", "Computer wins!")
        else:
            messagebox.showinfo("Tic Tac Toe", "You win!")
    elif " " not in [item for sublist in board for item in sublist]:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")

def minimax(board, depth, isMaximizing):
    if check_win(board):
        if isMaximizing:
            return {'score': -1}
        else:
            return {'score': 1}
    elif " " not in [item for sublist in board for item in sublist]:
        return {'score': 0}

    if isMaximizing:
        bestScore = {'score': -float('inf')}
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    score['move'] = {'i': i, 'j': j}
                    if score['score'] > bestScore['score']:
                        bestScore = score
        return bestScore
    else:
        bestScore = {'score': float('inf')}
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    score['move'] = {'i': i, 'j': j}
                    if score['score'] < bestScore['score']:
                        bestScore = score
        return bestScore

def computer_move(board):
    move = minimax(board, 0, True)['move']
    board[move['i']][move['j']] = "O"
    buttons[move['i']][move['j']].config(text="O", state="disabled")

def check_win(board):
    # check horizontal spaces
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # check vertical spaces
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            return True

    # check / diagonal spaces
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # check \ diagonal spaces
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

root = tk.Tk()
root.title("Tic Tac Toe")
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[tk.Button(root, text=" ", width=20, height=10, command=lambda row=i, col=j: click(row, col)) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

def restart_game():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text=" ", state="normal")

# Create the restart button
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

root.mainloop()