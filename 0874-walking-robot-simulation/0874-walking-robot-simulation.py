class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        def coors_inc():
            nonlocal drc, sr, sc
            dr, dc = drc[idx]
            return sr + dr, sc + dc
        
        def turn(turn_val):
            nonlocal idx
            if turn_val == -1:
                idx = (idx + 1) % 4
            else:
                idx -= 1
                if idx < 0:
                    idx = 3
            
        def eud(x1, y1, x2, y2):
            return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        
        drc = [(0,1), (1,0), (0,-1), (-1,0)]
        idx = 0
        points = set()
        obstacles = set([(x,y) for x,y in obstacles])
        sr = sc = 0
        for cmd in commands:
            if cmd < 0:
                turn(cmd)
            else:
                for _ in range(cmd):
                    nr, nc = coors_inc()
                    if (nr, nc) not in obstacles:
                        sr, sc = nr, nc
                        
            points.add((sr, sc))
        
        maxr = maxc = maxd = 0
        for x, y in points:
            dis = eud(0, 0, x, y)
            if dis > maxd:
                maxd = dis
                maxr, maxc = x, y
         
        
        return (maxr ** 2) + (maxc ** 2)
            
            
        
        
        
        
        
        
        
        
        