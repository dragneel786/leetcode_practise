class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def check_sub(i, j):
            if(i >= len(text1) or \
               j >= len(text2)):
                return 0
            
            ans = 0
            if(text1[i] == text2[j]):
                ans = 1 + check_sub(i + 1, j + 1)
            ans = max(ans, check_sub(i + 1, j), check_sub(i, j + 1))
            return ans
        
        return check_sub(0, 0)