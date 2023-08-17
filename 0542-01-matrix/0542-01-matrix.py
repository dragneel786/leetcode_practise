class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
       
        def init_op():
            for r in range(rows):
                ro = []
                for c in range(cols):
                    ap = inf
                    if(mat[r][c] == 0):
                        que.append((r,c,0))
                        ap = 0
                    
                    ro.append(ap)
            
                op.append(ro)
        
        
        def populate():
            while(que):
                sr, sc, dis = que.popleft()
                for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
                    nr, nc = sr + dr, sc + dc
                    if(0 <= nr < rows and 0 <= nc < cols\
                       and op[nr][nc] > dis + 1):
                        op[nr][nc] = dis + 1
                        que.append((nr, nc, dis + 1))
        
        rows, cols = len(mat), len(mat[0])
        que = deque()
        op = []
        init_op()
        populate()
        return op
        
                
        