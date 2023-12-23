class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        path_map = {'N':(-1, 0), 'E':(0, 1), 'W':(0,-1), 'S':(1, 0)}
        x = y = 0
        for p in path:
            dx, dy = path_map[p]
            nx, ny = x + dx, y + dy
            if((nx,ny) in visited):
                return True
            
            visited.add((nx, ny))
            x, y = nx, ny
        
        return False
            
            