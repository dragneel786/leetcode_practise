class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        indexes = {i for i in range(n)}
        
        for i in range(1, m):
            for j in range(n):
                if(j in indexes):
                    a, b = strs[i][j], strs[i - 1][j]
                    if(a < b):
                        indexes.remove(j)
        
        return n - len(indexes)
                        
            
        