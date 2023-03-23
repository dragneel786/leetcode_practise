class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def union(x, y):
            parents[x] = y
        
        def find(x):
            if(parents[x] != x):
                parents[x] = find(parents[x])
            return parents[x]
                
        parents = {i:i for i in range(n)}
        extra = dis = 0
        for a, b in connections:
            pa, pb = find(a), find(b)
            if(pa == pb):
                extra += 1
            else:
                union(pa, pb)
        
        
        for a, b in parents.items():
            dis += a == b
        
        return dis - 1 if(dis - 1 <= extra) else -1
                