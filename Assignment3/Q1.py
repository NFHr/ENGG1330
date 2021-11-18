import math
def fly(distance, station, start, end):
    if math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2) <= distance:
        return 'y'
    for i, s in enumerate(station):
        if math.sqrt((start[0] - s[0])**2 + (start[1] - s[1])**2) <= distance:
            if fly(distance, station[i+1:len(station)+1], s, end) == 'y':
                return 'y'
    else:
        return 'n'

def main():
    N, D = list(map(int, input().split()))
    station = tuple([map(int,input().split()) for i in range(N)])
    print(fly(D, station, tuple(map(int, input().split())),tuple(map(int,input().split()))))

main()