class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        allowed_moves = {
            1: {
                (0,1): [1,3,5],
                (0,-1): [1,4,6]
            },
            2: {
                (1,0): [2,5,6],
                (-1,0): [2,3,4]
            },
            3: {
                (1,0): [2,5,6],
                (0,-1): [1,4,6]
            },
            4: {
                (1,0): [2,5,6],
                (0,1): [1,3,5]
            },
            5: {
                (-1,0): [2,3,4],
                (0,-1): [1,4,6] 
            },
            6: {
                (0,1): [1,3,5], 
                (-1,0): [2,3,4]
            }
        }
        return self.is_valid_path(0, 0, grid, allowed_moves, set())

    def is_valid_path(self, x, y, grid, allowed_moves, visited):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return False

        if (x, y) in visited:
            return False
        
        if x == m - 1 and y == n - 1:
            return True

        val = grid[x][y]
        visited.add((x,y))
        for (dx, dy), value in allowed_moves[val].items():
            nx, ny = x + dx, y + dy
            if self.is_valid_path(nx, ny, grid, allowed_moves, visited)\
                 and grid[nx][ny] in value:
                return True

        return False