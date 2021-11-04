space, r, c, listA, listB, list_output, check = ' ', 6, 7, [], [' '], [], input('Standard game? (y/n): ')
if check == 'n':
    r,c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
if r >= 10 or c >= 10:
    listB, space = ['  '], '  '
    
for i in range(r):
    if ((r >= 10 or c >= 10) and r-i-1 <= 9):
        listA = [' ', r-i-1]
    else: 
        listA = [r-i-1]
    for n in range(c):
            listA += space, '·'
    listA += ' '
    list_output += [listA]
for k in range(c):
    if (r >= 10 or c >= 10) and k>= 10:
        listB += ' ', k
    else:
        listB += space, k
listB += ' '
list_output += [listB]
for j in list_output:
    for k in range(len(j)):
        print(j[k], end='')
    print()