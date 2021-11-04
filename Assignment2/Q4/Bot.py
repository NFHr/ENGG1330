import random


def convert(B):  # convert Board to 0, 1
    for Position in B:
        for k in range(9):
            if B[Position][k] == 'X':
                B[Position][k] = 1
            else:
                B[Position][k] = 0
    return B


def getR(l):  # get rotated list
    n = []
    for a in list(l):
        temp = [a]
        temp.append([a[6], a[3], a[0], a[7], a[4], a[1], a[8], a[5], a[2]])
        temp.append([a[8], a[7], a[6], a[5], a[4], a[3], a[2], a[1], a[0]])
        temp.append([a[2], a[5], a[8], a[1], a[4], a[7], a[0], a[3], a[6]])
        temp.append([a[2], a[1], a[0], a[5], a[4], a[3], a[8], a[7], a[6]])
        temp.append([a[2], a[1], a[0], a[5], a[4], a[3], a[8], a[7], a[6]])
        temp.append([a[6], a[7], a[8], a[3], a[4], a[5], a[0], a[1], a[2]])
        n.extend(temp)
    temp = []
    for item in n:
        if not item in temp:
            temp.append(item)
    return tuple(temp)


# fingerprint of the board
# Most of these cases are founded by print('UNKNOWN: ', tempBoard[k])
A = getR((
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1]))

B = getR((
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1]))

C = ([0, 0, 0, 0, 0, 0, 0, 0, 0],)

D = getR((
    [1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1]))

C2 = ([0, 0, 0, 0, 1, 0, 0, 0, 0],)

AD = getR((
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0]))

AB = getR((
    [1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 1, 0]))

winning = ([1, 0, 0, 0], [0, 2, 0, 0], [0, 1, 1, 0], [0, 0, 2, 0])


def copy(Board):  # prevent modification of the orginal list
    y = {}
    for x in Board:
        B = Board[x][:]
        y[x] = B
    return y


def getConfigurations(Board, P, M):
    configurations = [0, 0, 0, 0]  # a,b,c,d
    tempBoard = copy(Board)
    tempBoard[P][M] = 1
    for k in tempBoard:
        if tempBoard[k] in A:
            configurations[0] = configurations[0] + 1
        elif tempBoard[k] in B:
            configurations[1] = configurations[1] + 1
        elif tempBoard[k] in C:
            configurations[2] = configurations[2] + 1
        elif tempBoard[k] in D:
            configurations[3] = configurations[3] + 1
        elif tempBoard[k] in C2:
            configurations[2] = configurations[2] + 2
        elif tempBoard[k] in AD:
            configurations[0] = configurations[0] + 1
            configurations[3] = configurations[3] + 1
        elif tempBoard[k] in AB:
            configurations[0] = configurations[0] + 1
            configurations[1] = configurations[1] + 1
#        if configurations == [0, 0, 0, 0] and tempBoard[k] not in ONE:
#            print('UNKNOWN: ', tempBoard[k])
    if configurations in winning:
        return True
    else:
        return False


def AI(B):
    Move = []
    Board = convert(copy(B))
    for Position in Board:
        for n in range(9):
            if Board[Position][n] != 'X':
                if getConfigurations(Board, Position, n):
                    Move.append(f'{Position}{str(n)}')
    return random.choice(Move)
