def printBoard(Board):
    print('      '.join([k for k in Board]))
    for i in 0,3,6:
        line = ''
        for k in Board:
            line += f'{Board[k][i]} {Board[k][i+1]} {Board[k][i+2]}  '
        print(line.rstrip())

def judge(P, Position, Board, g):
    dead = False
    for i in range(3): # 横/竖/斜
        if g[i*3] == g[i*3 + 1] == g[i*3 + 2] or g[i] == g[i+3] == g[i+6] or g[0] == g[4] == g[8] or g[2] == g[4] == g[6]:
            dead = True
    if dead:
        if len(Board) == 1:
            print(f'Player {((P+1) % 2) + 1} wins game')
            return 1
        else:
            del Board[Position]
    return 0

def inputjudge(Board,P):
    while True:
        string = input(f'Player {P + 1}: ')
        if len(string) == 2 and string[0].isupper() and string[1].isdigit() and string[0] in Board:
            if 0 <= int(string[1]) <= 8:
                if Board[string[0]][int(string[1])] != 'X':
                    return string
        print('Invalid move, please input again')

def main():
    Board = {'A':list(range(9)), 'B':list(range(9)), 'C':list(range(9))}
    Player = 0
    while True:
        printBoard(Board)
        Position, move = inputjudge(Board, Player)
        Board[Position][int(move)] = 'X'
        if judge(Player, Position, Board, Board[Position]) == 1: 
            break
        Player = (Player+1) % 2
    return Player

main()