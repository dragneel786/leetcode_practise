class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vcounts = 0
        ans = 0
        for j, c in enumerate(s):
            if(j >= k):
                vcounts -= s[j - k] in vowels
                
            vcounts += c in vowels
            ans = max(ans, vcounts)
            if(ans == k):
                return ans
        
        return ans
            
            