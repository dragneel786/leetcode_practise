class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        maps = defaultdict(lambda:([0] * n))
        n = len(source)
        for i, c in enumerate(source):
            maps[c][i] = i + 1
        
        for c in maps.keys():
            for j in range(n - 2, -1, -1):
                if(not maps[c][j]):
                    maps[c][j] = maps[c][j + 1]
        
        j = 0
        counts = 1
        for c in target:
            if(not maps[c][0]): return -1
            
            if(j == n or not maps[c][j]):
                counts += 1
                j = 0
                
            j = maps[c][j]
        
        return counts
            
            