class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        def checkPalin(i, j, s):
            while(i <= j):
                if(s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True
        
        while(i < j):
            if(s[i] != s[j]):
                return checkPalin(i + 1, j, s) or \
                    checkPalin(i, j - 1, s)

            i += 1
            j -= 1
        
        return True
        
    