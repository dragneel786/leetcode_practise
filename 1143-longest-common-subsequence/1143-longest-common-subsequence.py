class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def lcs(i1, i2):
            nonlocal text1, text2
            if(i1 >= len(text1) or i2 >= len(text2)):
                return 0
            
            val = max(lcs(i1, i2 + 1), lcs(i1 + 1, i2))
            if(text1[i1] == text2[i2]):
                return max(val, 1 + lcs(i1 + 1, i2 + 1))
            
            return val
        
        return lcs(0, 0)