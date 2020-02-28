#can solve easy sodoku puzzles when a test of row col and subset square give the possbilities of remaining numbers as 1
import numpy as np




size = 9
originalgridEasy = [[2, 0, 0, 0, 7, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 2, 7, 3, 4],
                    [4, 6, 7, 0, 0, 8, 0, 0, 9],
                    [0, 0, 0, 9, 1, 0, 0, 0, 8],
                    [0, 1, 0, 0, 8, 7, 0, 0, 0],
                    [0, 8, 6, 2, 5, 4, 1, 0, 7],
                    [0, 0, 8, 3, 4, 0, 0, 2, 0],
                    [9, 4, 0, 0, 2, 0, 8, 5, 0],
                    [6, 5, 0, 0, 9, 0, 4, 0, 0]]

originalgridHard = [[9, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 3, 0, 2, 0, 0, 0, 0, 0],
                    [0, 1, 5, 3, 4, 0, 0, 7, 0],
                    [6, 0, 0, 1, 3, 0, 0, 4, 9],
                    [7, 0, 0, 0, 0, 0, 6, 0, 0],
                    [2, 0, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 3],
                    [0, 0, 0, 9, 1, 0, 0, 0, 0],
                    [0, 7, 9, 0, 8, 0, 0, 0, 0]]


# return a list of numbers in list
def availableNumbersInList(inlist):
    # print(inlist[0])

    availableNumbers = []
    for i in range(1, size + 1):
        if i not in inlist:
            availableNumbers.append(i)
    return availableNumbers


# get internal square as list
def getSmallSquare(grid, row, col, size=3):
    squareList = []
    rowStart = row // 3 * 3
    colStart = col // 3 * 3
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            val = grid[r, c]
            #print(val)
            squareList.append(val)
    return availableNumbersInList(squareList)

def commonElemeentsInList(a,b,c):
    result = [value for value in a if value in b and value in c]
    return result

def getCommonElementsByCoord(grid, row_x, col_y):
    availInRow = availableNumbersInList(grid_np[row_x, :])
    availInCol = availableNumbersInList(grid_np[:, col_y])
    availInSquare = getSmallSquare(grid_np, row_x, col_y)
    availableNumbers = commonElemeentsInList(availInRow, availInCol, availInSquare)
    return availableNumbers

def updateGrid(grid, row,col, val):
    grid_np[row][col] = val
    print("added values at row: ", row, " ,col: ", col, " , val: ", val)



def printSodoku(grid):
    for idx, x in enumerate(grid):
        if idx % 3 == 0 and idx != 0:
            print("\n------+-------+------", end=" ")
        for i in range(0, 9):
            # print("i: ", i)
            if i % 3 == 0 and i != 0:
                print("|", end=" ")
            elif i == 0:
                print("")
            print(x[i], end=" ")
    print("\n_______________________________-")


#convert to numpy array
grid_np = np.array(originalgridHard)

#Get Remaining
for w in range(0, 4):
    remaining = np.where(grid_np == 0)
    listOfRemaining = list(zip(remaining[0],remaining[1]))
    print("count of remaining: ", len(remaining[0]))
    for i in listOfRemaining:
        printSodoku(np.array(grid_np.tolist()))
        print("remaining cord to test: ", i)
        row = i[0]
        col = i[1]
        print("row: ", row, " , col: ", col)
        availableNumbers = getCommonElementsByCoord(grid_np,row,col)
        print("available numbers to use count: ", len(availableNumbers))
        if len(availableNumbers) == 1:
            updateGrid(grid_np, row,col,availableNumbers[0])

        print("available numbers than can be used", availableNumbers)
    remaining = np.where(grid_np == 0)
    listOfRemaining = list(zip(remaining[0],remaining[1]))
    print("count of remaining: ", len(remaining[0]))
    print("loop count: ",w)
    printSodoku(np.array(grid_np.tolist()))
for i in range(0, len(remaining)):
    print(grid_np[0][i])













