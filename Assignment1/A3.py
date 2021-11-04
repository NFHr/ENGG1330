slicing, startpos, fancypos = 1, 0, 0  #silcing adjust
r, c, standard = 6, 7, input('Standard game? (y/n): ') #initial variable
listA, listB, listfancy, list_output = [], [' '], [],[] #initial list
start, spaceA, spaceB = ' ', ' ', ' ' #space-controling

if standard == 'n': #input and check
    r,c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
fancy = input('Fancy board? (y/n): ')

if r >= 10 or c >= 10:
    listB, spaceA, spaceB = ['  '], '  ', '  '

if fancy == 'y':
    slicing, startpos, start = 2, 1, '|'
    listfancy = [spaceA]
    if (r >= 10 or c >= 10):
        spaceA = '| '
    else:
        spaceA = '|'
    for l in range(c):
        if (r >= 10 or c >= 10):
            listfancy += '+--'
        else:
            listfancy += '+-'
    listfancy += '+'

for i in range(r): #create rows
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

for k in range(c): #create row of columns
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

while True:
    player = 'X'
    move = input('playerX (col #): ')
    if move == 'e':
        break
    move = int(move) + 1

    if (r >= 10 or c >= 10): #large slicing starting position
        fancypos = 1
    else:
        fancypos = 0

    for x in range(1,len(list_output)):
        row = -x
        if row <= -11:
            fancypos = 0
        if list_output[startpos:len(list_output)-1:slicing][row][fancypos + (2 * move)] in ('X', 'O'):
           row -= 1
           continue
        else:
            list_output[startpos:len(list_output)-1:slicing][row][fancypos + (2 * move)] = player
            break
    for j in list_output:
        for k in range(len(j)):
            print(j[k], end='')
        print()

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

print('bye')