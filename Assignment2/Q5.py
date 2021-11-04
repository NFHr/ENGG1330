def createBoard():
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove(board, player):
    while True:
        printBoard(board)
        col = input( 'player'+ player +' (col #): ')
        if col == 'e':
            return 1
        else: 
            col = int(col)
        if board[len(board)-1][col] =='·':
                r = len(board)
                for row in range(r):
                    if board[row][col]!='·' and board[row+1][col]=='·':
                        board[row+1][col] = player
                        return
                    elif board[row][col]=='·':
                        board[row][col] = player
                        return

def judgeWinner(board, player):
    r, c = len(board), len(board[0])
    cases = board[:] #horizontal
    cases += [[board[i][i+index] for i in range(c) if i <= r-1 and i+index <= c-1] for index in range(r)] + [[board[i+index][i] for i in range(c) if i+index <= r-1 and i <= c-1] for index in range(r)] #diagonal starts from right
    cases += [[board[i][index-i] for i in range(r) if index - i >= 0 and i <= c-1] for index in range(c-1,-1,-1)] + [[board[index-i][i] for i in range(c) if index - i >= 0 and i <= c-1] for index in range(r-1,-1,-1)] #diagonal starts from left
    cases += [[board[row][col] for row in range(r)] for col in range(c)] #vertical

    for g in cases:
        count = 0
        for j in range(len(g)-1):
            if g[j] == g[j+1] and g[j] != '·':
                count += 1
                if count == 3:
                    printBoard(board)
                    print('Player', player, 'has won!')
                    return 1
            else:
                count = 0

def main():
    board = createBoard()
    for i in range(len(board) * len(board[0])):
        if i % 2 == 0: 
            player = 'X'
        else: 
            player = 'O'
            
        if makeMove(board, player) or judgeWinner(board, player):
            break
    else:
        printBoard(board)
        print('Draw!')
    print('bye')

main()