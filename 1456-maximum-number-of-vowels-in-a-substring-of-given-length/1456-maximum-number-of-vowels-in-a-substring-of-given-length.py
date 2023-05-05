class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vcounts = 0
        ans = 0
        i = 0
        for j, c in enumerate(s):
            if(j - i + 1 > k):
                vcounts -= s[i] in vowels
                i += 1
            
            vcounts += c in vowels
            ans = max(ans, vcounts)
        
        return ans
            
            