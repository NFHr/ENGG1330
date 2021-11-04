m, n = list(map(int,input().split()))
numlist = []
temp = 0
perfect = []
for i in range(m,n):
    temp = 0

    for j in range(1,i):
        if i % j == 0:
            temp += j

    if temp == i:
        perfect.append(i)

if len(perfect) != 0:
    if len(perfect) == 1:
        print(perfect[0])
    else:
        for i in range(len(perfect)):
            if i == 0:
                print(perfect[i], end = '')
            elif i != len(perfect-1):
                print(' ' + str(perfect[i]), end=' ')
            else:
                print(' ' + str(perfect[i]))

