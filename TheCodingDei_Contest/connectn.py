"""
    Solution to Connect-N problem: https://open.kattis.com/problems/connectn
    Author: Francesco Pham
    Date: 13/12/2019
"""
X, Y, N = [int(x) for x in input().split()]
board = []
for _ in range(X):
    board.append(input().split())

winner = "NONE"

#check rows
for i in range(X):
    consecutives = 0
    for j in range(Y):
        if board[i][j] != 'O' and (j==0 or board[i][j] == board[i][j-1]):
            consecutives += 1
            if consecutives == N:
                if board[i][j] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[i][j] != 'O':
            consecutives = 1
        else:
            consecutives = 0

#check columns
for j in range(Y):
    consecutives = 0
    for i in range(X):
        if board[i][j] != 'O' and (i==0 or board[i][j] == board[i-1][j]):
            consecutives += 1
            if consecutives == N:
                if board[i][j] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[i][j] != 'O':
            consecutives = 1
        else:
            consecutives = 0

#check diagonals from top left to bottom right
for i in range(Y):
    x = 0
    y = i
    consecutives = 0
    while x < X and y < Y:
        if board[x][y] != 'O' and (x==0 or y==0 or board[x][y] == board[x-1][y-1]):
            consecutives += 1
            if consecutives == N:
                if board[x][y] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[x][y] != 'O':
            consecutives = 1
        else:
            consecutives = 0

        x += 1
        y += 1

for i in range(X):
    x = i
    y = 0
    consecutives = 0
    while x < X and y < Y:
        if board[x][y] != 'O' and (x==0 or y==0 or board[x][y] == board[x-1][y-1]):
            consecutives += 1
            if consecutives == N:
                if board[x][y] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[x][y] != 'O':
            consecutives = 1
        else:
            consecutives = 0
        
        x += 1
        y += 1

# check diagonals from top right to bottom left
for i in range(Y):
    x = 0
    y = i
    consecutives = 0
    while x < X and y >= 0:
        if board[x][y] != 'O' and (x==0 or y==Y-1 or board[x][y] == board[x-1][y+1]):
            consecutives += 1
            if consecutives == N:
                if board[x][y] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[x][y] != 'O':
            consecutives = 1
        else:
            consecutives = 0

        x += 1
        y -= 1

for i in range(X):
    x = i
    y = Y-1
    consecutives = 0
    while x < X and y >= 0:
        if board[x][y] != 'O' and (x==0 or y==Y-1 or board[x][y] == board[x-1][y+1]):
            consecutives += 1
            if consecutives == N:
                if board[x][y] == 'B':
                    winner = "BLUE WINS"
                else:
                    winner = "RED WINS"
        elif board[x][y] != 'O':
            consecutives = 1
        else:
            consecutives = 0
        
        x += 1
        y -= 1

print(winner)