class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nx, ny = find(x), find(y)
            if(nx != ny):
                parent[ny] = nx
        
        
        parent = {chr(97 + i):chr(97 + i) for i in range(26)}
        for e in equations:
            if(e[1] == "="):
                union(e[0], e[3])
        
        for e in equations:
            if(e[1] == '!' and find(e[0]) == find(e[3])):
                return False
        return True
                