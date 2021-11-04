start, spaceA, spaceB, r, c, listA, listB, listfancy, list_output, standard = ' ', ' ', ' ', 6, 7, [], [' '], [],[], input('Standard game? (y/n): ')

if standard == 'n':
    r,c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    
fancy = input('Fancy board? (y/n): ')

if r >= 10 or c >= 10:
    listB, spaceA, spaceB = ['  '], '  ', '  '

if fancy == 'y':
    listfancy = [spaceA]
    start = '|'
    if (r >= 10 or c >= 10):
        spaceA = '| '
    else:
        spaceA = '|'
    for l in range(c):
        if (r >= 10 or c >= 10):
            listfancy += '+', '-', '-'
        else:
            listfancy += '+', '-'
    listfancy += '+'

for i in range(r):
    if fancy == 'y':
        list_output += [listfancy]
    if ((r >= 10 or c >= 10) and r-i-1 <= 9):
        listA = [' ', r-i-1]
    else: 
        listA = [r-i-1]
    for n in range(c):
            listA += spaceA, '·'
    listA += start
    list_output += [listA]

for k in range(c):
    if (r >= 10 or c >= 10) and k>= 10:
        listB += ' ', k
    else:
        listB += spaceB, k
listB += ' '
if fancy == 'y':
    list_output += [listfancy]
list_output += [listB]

for j in list_output:
    for k in range(len(j)):
        print(j[k], end='')
    print()