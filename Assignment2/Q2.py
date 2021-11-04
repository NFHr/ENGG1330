def printBoard(size, Board):
    k = 0
    while k != size ** 2:
        x = ''
        for _ in range(size):
            x += f'{Board[k]:>2} '
            k += 1
        print(x.rstrip())

def judge(Board, Player, count, size):
    cases = [[Board[i*size+i] for i in range(size)]] + [[Board[(size-i-1)*size+i] for i in range(size)]] #斜
    for i in range(size):
        cases += [Board[i*size:i*size+size]] + [[Board[i+size*j] for j in range(size)]] #横+竖
    for k in cases: #判断
        if len(set(k)) == 1:
            return Player
    if count == size ** 2: #平局
        return 'None'
    return 0

def main():
    size = int(input('Size--> '))
    Board = [x for x in range(size ** 2)]
    print(Board)
    printBoard(size, Board)
    count, Player = 0, 'X'

    while not judge(Board, Player, count, size):
        if count % 2 == 0:
            Player = 'X'
        else:
            Player = 'O'
        Board[int(input(f'{Player}--> '))] = Player
        printBoard(size, Board)
        count += 1
    print('Winner:', judge(Board, Player, count, size))

main()