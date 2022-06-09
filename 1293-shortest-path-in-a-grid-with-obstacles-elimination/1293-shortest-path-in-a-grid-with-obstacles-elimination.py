class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if(k >= m + n - 2):
            return m + n - 2
        
        state = (0, 0, k)
        st = deque([(0, state)])
        visited = set([state])
        while(st):
            steps, (px, py, k) = st.popleft()

            if((px, py) == (m - 1, n - 1)):
                return steps

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x, y = px + dx, py + dy

                if(0 <= x < m and 0 <= y < n):
                    ne = k - grid[x][y]
                    newState = (x, y, ne)
                    if(ne >= 0 and newState not in visited):
                        st.append((steps + 1, newState))
                        visited.add(newState)
        return -1