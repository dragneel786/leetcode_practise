class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        dire = {'E':(0,1), 'W':(0,-1),
                'N':(-1,0), 'S':(1, 0)}
        
        sr = sc = 0
        for p in path:
            dr, dc = dire[p]
            sr, sc = sr + dr, sc + dc
            if((sr, sc) in visited):
                return True
            
            visited.add((sr, sc))
            
        return False