class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        while(i < j):
            while(not s[i].isalnum()):
                i += 1
                if(i > j):
                    return True
            ch1 = s[i].lower()

            while(not s[j].isalnum()):
                j -= 1
                if(j < i):
                    return True
            ch2 = s[j].lower()
            
            if(ch1 == ch2):
                i += 1
                j -= 1
            else:
                return False
        
        return True
            
            
            
            
        