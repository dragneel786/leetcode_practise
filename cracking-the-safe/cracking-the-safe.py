class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        def dfs(start):
            nonlocal res, k
            for c in range(k):
                ch = str(c)
                node = start + ch
                
                if(node not in visited):
                    visited.add(node)
                    dfs(node[1:])
                    res += ch
                
        if(n == 1 and k == 1):
            return '0'
        
        visited = set()
        temp = '0' * (n - 1)
        res = ''
        dfs(temp)
        res += temp
        return res
        