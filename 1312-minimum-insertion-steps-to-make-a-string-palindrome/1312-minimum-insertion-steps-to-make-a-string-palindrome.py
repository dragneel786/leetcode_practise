class Solution:
    def minInsertions(self, s: str) -> int:
        
        @lru_cache(None)
        def min_oper(i, j):
            if(i >= j):
                return 0
            
            if(s[i] != s[j]):
                return min(min_oper(i + 1, j),\
                           min_oper(i, j - 1)) + 1
            
            return min_oper(i + 1, j - 1)
        
        return min_oper(0, len(s) - 1)
                
        