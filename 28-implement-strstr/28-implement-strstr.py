class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(not needle):
            return 0
        
        m = len(haystack)
        n = len(needle)
    
        if(n > m):
            return -1
        
        for i in range(m - n + 1):
            if(haystack[i: i + n] == needle):
                return i
        
        return -1