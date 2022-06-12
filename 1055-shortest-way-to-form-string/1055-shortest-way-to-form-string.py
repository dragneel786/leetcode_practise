class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        maps = dict()
        n = len(source)
        for i, c in enumerate(source):
            if(c not in maps):
                maps[c] = ([0] * n)
            maps[c][i] = i + 1
        
        for c in maps.keys():
            prev = 0
            for j in range(n - 1, -1, -1):
                if(maps[c][j]):
                    prev = maps[c][j]
                maps[c][j] = prev
        
        
        j = 0
        counts = 1
        for c in target:
            if(c not in maps): return -1
            
            if(j == n or not maps[c][j]):
                counts += 1
                j = 0
                
            j = maps[c][j]
        
        return counts
            
            