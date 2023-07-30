class Solution:
    def strangePrinter(self, s: str) -> int:
        
        @lru_cache(None)
        def solve(i, j):
            if(i == j):
                return 1
            
            min_ans = inf
            for k in range(i, j):
                min_ans = min(solve(i, k) + solve(k + 1, j),\
                              min_ans)
            
            return min_ans - (s[i] == s[j])
        
        
        return solve(0, len(s) - 1)
    