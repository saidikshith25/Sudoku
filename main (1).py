M=9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    startRow=row- row % 3
    startCol=col- col % 3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol]==num:
                return False
    return True
def Sudoku(grid, row, col):
    if (row==M-1 and col == M):
        return True
    if col==M:
        row+=1 
        col= 0
    if grid[row][col]>0:
        return Sudoku(grid,row,col+1)
    for num in range(1,M+1,1):
        if solve(grid,row,col,num):
            grid[row][col]=num
            if Sudoku(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
grid=[[4,0,2,8,0,0,1,6,0],
[8,0,0,2,0,9,5,4,0],
[0,0,0,0,4,0,2,8,0],
[9,4,1,0,2,0,8,3,5],
[2,0,0,3,8,4,6,9,1],
[6,8,3,0,9,0,4,7,2],
[7,0,8,0,0,0,9,2,4],
[3,2,4,9,0,8,7,0,6],
[0,0,0,4,7,2,3,0,8]]
if(Sudoku(grid,0,0)):
    puzzle(grid)
else:
    print("No Solution exist:")