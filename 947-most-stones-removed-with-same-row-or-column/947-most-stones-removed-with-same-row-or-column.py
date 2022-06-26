class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict(lambda:None)
        col = defaultdict(lambda:None)
        n = len(stones)
        parent = [i for i in range(n)]

        def union(x, y):
            nx, ny = find(x), find(y)
            if(nx != ny):
                parent[ny] = nx

        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]

        for i,p in enumerate(stones):
            if(row[p[0]] != None):
                union(row[p[0]], i)

            if(col[p[1]] != None):
                union(col[p[1]], i)

            col[p[1]] = i
            row[p[0]] = i

        count = 0
        for i in range(n):
            if(parent[i] != i):
                count += 1
        return count
        
        
                
                
                
        