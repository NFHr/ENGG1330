def generate(g):
    print('|', g[1], '||', g[2], '||', g[3], '|')
    print('|', g[4], '||', g[5], '||', g[6], '|')
    print('|', g[7], '||', g[8], '||', g[9], '|')

def inputjudge(pos,g):
    if not pos.isdigit():
        print('Error: invalid input')
        return False
    elif int(pos) >= 10 or int(pos) <= 0:
        print('Error: invalid input')
        return False
    else:
        pos = int(pos)
    if g[pos] == 'X' or g[pos] == 'O':
        print('Error: N/A position')
        return False
    else:
        return pos

def play(player, g):
    while True:
        pos = inputjudge(input(f'{player}: '), g)
        if pos:
            g[pos] = player
            generate(g)
            break
        else:
            generate(g)
            continue
            
def judge(g):
    j = 0
    for i in range(1,10):
        if g[i] == 'X' or g[i] == 'O':
            j += 1
    if j == 9:
        print('Tie')
        return True
    for i in 0, 3, 6:
        if g[i+1] == g[i+2] == g[i+3]:
            print(f'Player {g[i+1]} wins')
            return True
    for i in 1, 2, 3:
        if g[i] == g[i+3] == g[i+6]:
            print(f'Player {g[i]} wins')
            return True
    if g[1] == g[5] == g[9] or g[3] == g[5] == g[7]:
        print(f'Player {g[i]} wins')
        return True
    return False

def main():
    g = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
    generate(g)
    while True:
        play('X', g)
        if judge(g):
            break
        play('O', g)
        if judge(g):
            break


main()