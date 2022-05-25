class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(x, y):
            st = deque()
            st.append((x, y))
            while(len(st)):
                for _ in range(len(st)):
                    node = st.pop()
                    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        xi, yi = node[0] + di, node[1] + dj
                        if(0 <= xi < rows and 0 <= yi < cols and grid[xi][yi] != "0"):
                            grid[xi][yi] = "0"
                            st.append((xi, yi))
            
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1"):
                    islands += 1
                    grid[r][c] = "0"
                    bfs(r, c)
        return islands