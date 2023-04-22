class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        def min_oper(i, j):
            if(i >= j):
                return 0
            
            key = (i, j)
            if(key not in memo):
                if(s[i] != s[j]):
                    memo[key] = min(min_oper(i + 1, j),\
                                    min_oper(i, j - 1)) + 1
                else: 
                    memo[key] = min_oper(i + 1, j - 1)
        
            return memo[key]
        
        memo = dict()
        return min_oper(0, len(s) - 1)
                
        