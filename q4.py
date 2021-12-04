def rotation(t):
    rotated = list(zip(*t))[::-1]
    return rotated

def find(t):
    for i in range(len(M)):
        for j in range(len(M)):
            if i < len(M):
                k = M[i][j:j+len(t)]
                if tuple(M[i][j:j+len(t)]) == t[0]:
                    if then(i,j,t):
                        return 1
    else:
        if find(rotation(t)):
            return 1

def then(i,j,t):
    index = i
    count = 0
    for n in range(len(t)):
        if index < len(M):
            k = M[index][j:j+len(t)]
            if tuple(M[index][j:j+len(t)]) == t[n]:
                index += 1
                count +=1
    if count == len(t):
        F.append((j,i))
        return 1
    else:
        return 0

F = []
T = [tuple(input())]
for _ in range(len(T[0])-1):
    T.append(tuple(input()))
M = [tuple(input())]
for _ in range(len(M[0])-1):
    M.append(tuple(input()))
find(T)
print(F[0][0],F[0][1])