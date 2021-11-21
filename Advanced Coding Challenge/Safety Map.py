def find(y, x, Map, i):
    Block = []
    x1, x2 = x-i, x+i+1
    y1, y2 = y-i, y+i+1
    if x1 < 0:  x1 = 0
    if y1 < 0:  y1 = 0
    if x2 > len(Map):   x2 = len(Map)
    if y2 > len(Map):   y2 = len(Map)
    for i in range(y1, y2):
        Block += (Map[i][x1:x2])
    return Block

def main():
    Map = [[int(x) for x in input()]]
    Map += [[int(x) for x in input()] for _ in range(len(Map[0])-1)]
    SMap = [['0']*len(Map[0]) for _ in Map[0]]
    for y in range(len(Map)):
        for x in range(len(Map)):
            if Map[y][x] == 1:
                SMap[y][x] = '#'
            elif any(find(y, x, Map, 1)) == False:
                if any(find(y, x, Map, 2)):
                    SMap[y][x] = '1'
                else:
                    SMap[y][x] = '2'
    for i in SMap:
        print(''.join([j for j in i]))

main()