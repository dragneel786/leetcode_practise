class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
    
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
            
        parent = {i:i for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    union(i, j)
        
        counts = 0
        for i, _ in enumerate(isConnected):
            if parent[i] == i:
                counts += 1
        
        return counts
            
    
                