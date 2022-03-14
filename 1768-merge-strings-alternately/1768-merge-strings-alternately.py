class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        ans = ""
        while(i < m or j < n):
            if(i < m):
                ans += word1[i]
            
            if(j < n):
                ans += word2[j]
            
            i += 1
            j += 1
    
        return ans