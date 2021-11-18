def rorate(t):
    t = list(reversed(t))
    for i in range(len(t)):
        for j in range(i+1, len(t[i])):
            t[i][j], t[j][i] = t[j][i], t[i][j]
    return t

def find(nmap, ntreasure, k): #check map[0] with treasure[k]
    if len(nmap) == 0: return 1
    if nmap[0] == ntreasure[k] and find(nmap[1:len(nmap)], ntreasure, k+1): return 1
    else: return 0

#k is the index of the treasure
def locate(nmap, ntreasure, k):
    for index in range(len(nmap)-len(ntreasure)+1):
        for i in range(len(nmap)-len(ntreasure)+1):
            if nmap[index][i:i+len(ntreasure)] == ntreasure[k]:
                if find([x[i:i+len(ntreasure)] for x in nmap[index+1:index+len(ntreasure)]], ntreasure, k+1): #slicing map by the size of treasure
                    pos = (i, index)
                    return pos
    else:
        pos = locate(mapp, rorate(ntreasure), 0)
        if pos: return pos

treasure = [[int(i) for i in input()]]
treasure += [[int(j) for j in input()] for _ in range(len(treasure[0])-1)]
mapp = [[int(i) for i in input()]]
mapp += [[int(j) for j in input()] for _ in range(len(mapp[0])-1)]
print(' '.join(list(map(str, locate(mapp, treasure, 0)))))