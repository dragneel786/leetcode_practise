class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if(isWater[i][j] == 1):
                    height[i][j] = 0
                    dq.append((i, j))
    
        dire = [0, 1, 0, -1, 0]
        while(dq):
            r, c = dq.popleft()
            for i in range(4):
                nr, nc = r + dire[i], c + dire[i + 1]
                if(0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1):
                    height[nr][nc] = height[r][c] + 1
                    dq.append((nr, nc))
                
        
        return height
                    
        