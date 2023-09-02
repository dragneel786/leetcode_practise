class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @lru_cache(None)
        def dp(start):
            if(start == n):
                return 0
            
            min_val = dp(start + 1) + 1
            for end in range(start, n + 1):
                curr = s[start: end]
                if(curr in dset):
                    min_val = min(min_val, dp(end))
                
            return min_val
         
        dset = set(dictionary)
        n = len(s)
        return dp(0)