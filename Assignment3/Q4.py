def rorate(t):
    t = list(reversed(t))
    for i in range(len(t)):
        for j in range(i+1, len(t[i])):
            t[i][j], t[j][i] = t[j][i], t[i][j]
    return t

def find(NMap, Treasure, k):  # check map[0] with treasure[k]
    if len(NMap) == 0:
        return 1
    if NMap[0] == Treasure[k] and find(NMap[1:len(NMap)], Treasure, k+1):
        return 1
    else:
        return 0

# k is the index of the treasure

def locate(NMap, Treasure, k):
    for index in range(len(NMap)-len(Treasure)+1):
        for i in range(len(NMap)-len(Treasure)+1):
            if NMap[index][i:i+len(Treasure)] == Treasure[k]:
                # slicing map by the size of treasure
                if find([x[i:i+len(Treasure)] for x in NMap[index+1:index+len(Treasure)]], Treasure, k+1):
                    pos = (i, index)
                    return pos
    else:
        pos = locate(M, rorate(Treasure), 0)
        if pos:
            return pos

def main():
    global M
    T = [[int(i) for i in input()]]
    T += [[int(j) for j in input()] for _ in range(len(T[0])-1)]
    M = [[int(i) for i in input()]]
    M += [[int(j) for j in input()] for _ in range(len(M[0])-1)]
    print(' '.join(list(map(str, locate(M, T, 0)))))

main()