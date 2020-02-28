#can solve easy sodoku puzzles when a test of row col and subset square give the possbilities of remaining numbers as 1
#start as sane code as solver2 decided to wedge in a pygame for better visual of puzzle not great but differnt than the console output

import numpy as np
import pygame



pygame.init()
#myFont = pygame.font.SysFont("monospace", 15)
myFont = pygame.font.Font(pygame.font.get_default_font(), 15)
xdim = 500
ydim = 500
window = pygame.display.set_mode((xdim, ydim))
pygame.display.set_caption("Sodoku")




gridsize = 9
squareSize = 3

#generate font obj
numFontObj = []
for f in range(0,9+1):
    numFontObj.append(myFont.render(str(f), 1,(255,255,255)))

#generate grid
def renderGridPattern():
    for i in range(0,gridsize+1):
        width = 1
        if i % 3 == 0:
            width = 3
        pygame.draw.line(window,(255,255,255),(50 * i ,0), (50* i, 450),width)
        pygame.draw.line(window, (255, 255, 255), (0, 50 * i ), (450, 50 * i), width)
        #pygame.display.update()

def renderText(intVal, rowx, coly):
    window.blit(numFontObj[intVal], (22 + coly * 50, 22 + rowx * 50))
    #pygame.display.update()

def renderFullGrid():
    window.fill((0,0,0))
    renderGridPattern()
    for x in range(0,9):
        for y in range(0,9):
            renderText(grid_np[x][y],x,y)
    pygame.display.update()
    pygame.time.wait(10)

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

grid              =[[0,0,4,3,0,0,2,0,9],
                    [0,0,5,0,0,9,0,0,1],
                    [0,7,0,0,6,0,0,4,3],
                    [0,0,6,0,0,2,0,8,7],
                    [1,9,0,0,0,7,4,0,0],
                    [0,5,0,0,8,3,0,0,0],
                    [6,0,0,0,0,0,1,0,5],
                    [0,0,3,5,0,8,6,9,0],
                    [0,4,2,9,1,0,3,0,0]]

#convert to numpy array
grid_np = np.array(grid)
renderFullGrid()


# return a list of numbers in list
def availableNumbersInList(inlist):
    # print(inlist[0])

    availableNumbers = []
    for i in range(1, gridsize + 1):
        if i not in inlist:
            availableNumbers.append(i)
    return availableNumbers


# get internal square as list
def getSmallSquare(grid, row, col, squareSize=3):
    squareList = []
    rowStart = row // 3 * 3
    colStart = col // 3 * 3
    for r in range(rowStart, rowStart + squareSize):
        for c in range(colStart, colStart + squareSize):
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


#incomplete test
def checkneighborRows(grid, row, col):
    squareList = []
    rowStart = row // 3 * 3
    colStart = col // 3 * 3
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            val = grid[r, c]
            # print(val)
            squareList.append(val)
    return availableNumbersInList(squareList)

#incomplete
def checkneighborCols():
    print()



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


def solveWithBacktracking(grid_np):
    remaining = np.where(grid_np == 0)
    #if no remaining we are done
    if len(remaining[0]) == 0:
        return True
    row = remaining[0][0]
    col = remaining[1][0]

    availableNumbers = getCommonElementsByCoord(grid_np, row, col)
    for avail in availableNumbers:
        grid_np[row][col] = avail
        renderFullGrid()
        if(solveWithBacktracking(grid_np)):
            return True

        #not correct reset value to 0
        grid_np[row][col] = 0

    print("row: ", row, ", col: ", col)
    return False



totalAdded = 0
#Get Remaining
while True:
    solveWithBacktracking(grid_np)
    remaining = np.where(grid_np == 0)
    listOfRemaining = list(zip(remaining[0],remaining[1]))
    initialRemaining = len(remaining[0])
    print("count of intial remaining: ", initialRemaining)
    for i in listOfRemaining:
        #printSodoku(np.array(grid_np.tolist()))
        #print("remaining cord to test: ", i)
        row = i[0]
        col = i[1]
        #print("row: ", row, " , col: ", col)
        availableNumbers = getCommonElementsByCoord(grid_np,row,col)
        #print("available numbers to use count: ", len(availableNumbers))
        if len(availableNumbers) == 1:
            updateGrid(grid_np, row,col,availableNumbers[0])
            totalAdded += 1

        #print("available numbers than can be used", availableNumbers)
        renderFullGrid()
    remaining = np.where(grid_np == 0)
    listOfRemaining = list(zip(remaining[0],remaining[1]))
    endRemainingCount = len(remaining[0])
    print("count of remaining at end ", endRemainingCount)
    print("added solutions: ", totalAdded)
    printSodoku(np.array(grid_np.tolist()))
    if (endRemainingCount - initialRemaining) == 0:
        break
for i in range(0, len(remaining)):
    print(grid_np[0][i])

renderFullGrid()
solveWithBacktracking(grid_np)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








