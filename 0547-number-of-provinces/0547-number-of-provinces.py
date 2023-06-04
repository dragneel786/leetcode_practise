class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # [[1,1,0],
        #  [1,1,0],
        #  [0,0,1]]
        def union(x, y):
            px, py = find(x), find(y)
            if(px != py):
                parent[py] = px
            
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        n = len(isConnected)
        parent = {i:i for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if(isConnected[i][j]):
                    union(i, j)
        
        return sum([k==v for k, v in parent.items()])