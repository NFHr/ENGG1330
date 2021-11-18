def Queen(N, Board, x, y):
    up, dn, lt, rt = x, x, y, y
    Board[x] = [1] * N
    for i in range(N):
        Board[i][y] = 1
        if up <= N-1 and lt >= 0:   Board[up][lt] = 1
        if up <= N-1 and rt <= N-1: Board[up][rt] = 1
        if dn >= 0 and lt >= 0:     Board[dn][lt] = 1
        if dn >= 0 and rt <= N-1:   Board[dn][rt] = 1
        up, dn, lt, rt = up+1, dn-1, lt-1, rt+1

def main():
    N, M = list(map(int, input().split()))
    Board = [[0]*N for _ in range(N)]
    for _ in range(M):
        Queen(N, Board, *[i - 1 for i in list(map(int, input().split()))])
    print(sum([row.count(0) for row in Board]))

main()