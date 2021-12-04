#To count the number of free slots in the area marked by (startRow, startCol) - the top left slot, and (side) - the width of area 
def noOfFreeSlots(board, startRow, startCol, n):
    #width is the width of one area in terms of number of slots
    width = int((2**n)/2)
    count=0
    for i in range(startRow, startRow+width):
        for j in range(startCol, startCol+width):
            if board[i][j]==0:
                count+=1
    return count

#To find the area (top left(1), top right(2), bottom left(3), bottom right(4)) with a slot removed
def areaWithSlotRemoved(board,startRow,startCol, n):
    #width is the width of one area in terms of number of slots
    width = int((2**n)/2)
    if (noOfFreeSlots(board,startRow,startCol,n)!=(width**2)):
        print("Area 1 has slot removed")
        return 1
    elif (noOfFreeSlots(board,startRow,startCol+width,n)!=(width**2)):
        print("Area 2 has slot removed")
        return 2
    elif (noOfFreeSlots(board,startRow+width,startCol,n)!=(width**2)):
        print("Area 3 has slot removed")
        return 3
    else: 
        return 4

#To fill tile in the middle of the area
#area - the area with a cell removed
def fillTile(board,n,startRow,startCol,area):
    global tileNo
    tileNo += 1
    #width is the width of the area in terms of number of slots
    width = int((2**n)/2)
    
    if area==1:
        board[startRow+width-1][startCol+width]=tileNo
        board[startRow+width][startCol+width]=tileNo
        board[startRow+width][startCol+width-1]=tileNo
    elif area==2:
        board[startRow+width-1][startCol+width-1]=tileNo
        board[startRow+width][startCol+width-1]=tileNo
        board[startRow+width][startCol+width]=tileNo        
    elif area==3:
        board[startRow+width-1][startCol+width-1]=tileNo
        board[startRow+width-1][startCol+width]=tileNo
        board[startRow+width][startCol+width]=tileNo           
    else:
        board[startRow+width-1][startCol+width-1]=tileNo
        board[startRow+width-1][startCol+width]=tileNo
        board[startRow+width][startCol+width-1]=tileNo    
    
def initializeBoard(board,n):
    for i in range(2**n):
        board[i]=[0]*(2**n)

def printBoard(board,n):
    #width is the width of the printing area 
    width=2**n
    for i in range(width):
        #print (("%2i "*width)%tuple(board[i]))   # This is an alternative approach to print the entire row
        for j in board[i]:
            print (f'{j:^3}',end='')
        print()

#triominoes is a function that receives
#board - the board 2D array
#n - 2**n is the width of the working area of the board
#startRow,startCol is the top left corner slot of the working area concerned (as we will divide the board in sub area in recursive calls)
def triominoes(board,n,startRow=0,startCol=0):
    #base case
    if n==1:
        #print("Base case reached")
        area=areaWithSlotRemoved(board,startRow,startCol,n)
        fillTile(board,n,startRow,startCol,area)
    #progress
    else:
        #print("Case when n="+str(n)+"Tile number"+str(tileNo))
        area=areaWithSlotRemoved(board,startRow,startCol,n)
        #Fill in the middle tile
        fillTile(board,n,startRow,startCol,area)
        #width is the width of one area in terms of number of slots
        width = int((2**n)/2)
        #Recursively call the function for the 4 partition (smaller board)
        triominoes(board,n-1,startRow,startCol)
        triominoes(board,n-1,startRow,startCol+width)
        triominoes(board,n-1,startRow+width,startCol)
        triominoes(board,n-1,startRow+width,startCol+width)
        

    return

tileNo=0

def main():
    board={}
    initializeBoard(board,4)
    board[14][5]=-1
    printBoard(board,4)
    triominoes(board,4)
    printBoard(board,4)
    return

main()
