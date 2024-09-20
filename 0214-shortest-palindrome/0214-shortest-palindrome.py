class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rs = s[::-1]
        for i in range(len(s)):
            # print(s[:len(s) - i], rs[i:])
            if s[:len(s) - i] == rs[i:]:
                return rs[:i] + s
        
        return ""
        
    
    
                
        