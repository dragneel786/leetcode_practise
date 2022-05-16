class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if(grid[n - 1][n - 1] or grid[0][0]):
            return -1
        
        visited = set()
        st = deque()
        st.append((0, 0))
        visited.add((0, 0))
        path = 1
        while(len(st)):
            for _ in range(len(st)):
                node = st.pop()
                if(node == (n - 1, n - 1)):
                    return path
                for dx, dy in [[1,0], [-1,0], [0,1], [0,-1],\
                              [1,-1], [-1,1], [1,1],[-1,-1]]:
                    x = node[0] - dx
                    y = node[1] - dy
                    if(x >= n or x < 0 or y < 0 or y >= n \
                       or (x, y) in visited or grid[x][y]):
                        continue
                    st.appendleft((x, y))
                    visited.add((x, y))
            path += 1
        
        return -1
        
        