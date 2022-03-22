from queue import Queue
def updateMatrix(mat):
    q = Queue()
    rows = len(mat)
    cols = len(mat[0])
    for r in range(rows):
        for c in range(rows):
            if(not mat[r][c]):
                q.put((r, c))
            else:
                mat[r][c] = float("inf")
  
    while(not q.empty()):
        r, c = q.get()
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if(i >= 0 and j >= 0 and i < rows and j < cols and mat[i][j] > mat[r][c] + 1):
                q.put((i, j))
                mat[i][j] = mat[r][c] + 1
            
    return mat





print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))