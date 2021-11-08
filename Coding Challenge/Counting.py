str = input('String: ')
repeated = []

for i in str:
    if i not in repeated:
        repeated.append(i)

for i in repeated:
    temp = 0
    for j in str:
        if i == j:
            temp += 1
    print(i,temp)
