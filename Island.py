from queue import Queue
def maxAreaOfIsland(grid) -> int:
    q = Queue()
    rows = len(grid)
    cols = len(grid[0])
    maxArea = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                q.put((row, col))
                grid[row][col] = -1
                maxArea = max(maxArea, islandAreaFound(grid, q))

    return maxArea
    
def islandAreaFound(grid, q):
    area = 0
    rows = len(grid)
    cols = len(grid[0])
    while(q.qsize()):
        row, col = q.get()
        for i, j in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
            if(i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1):
                continue
            q.put((i, j))
            grid[i][j] = -1
        area += 1
        

    return area
print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))