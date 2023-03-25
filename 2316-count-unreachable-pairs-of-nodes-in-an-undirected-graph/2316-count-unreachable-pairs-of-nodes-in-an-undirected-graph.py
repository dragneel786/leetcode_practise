class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        
        def union(x, y):
            x, y = find(x), find(y)
            if(x != y):
                parent[x] = y
        
        
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            
            return parent[x]
        
        
        parent = {i:i for i in range(n)}
        for a, b in edges:
            union(a, b)
        
        groups = Counter()
        for i in range(n):
            groups[find(i)] += 1
        
        ans = 0
        for v in list(groups.values())[:-1]:
            n = n - v
            ans += v * n         
        
        return ans
        
        
        
        
        
        
        
            