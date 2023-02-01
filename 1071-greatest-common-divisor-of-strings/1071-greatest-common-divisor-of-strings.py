class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        if(m > n):
            return self.gcdOfStrings(str2, str1)
        
        if(set(str1) != set(str2)):
            return ''
        
        chars = list(str2)
        ts = str2
        while(chars and (ts * (n // len(chars)) != str1 or \
                        ts * (m // len(chars)) != str2)):
            chars.pop()
            ts = ''.join(chars)
        
        return ''.join(chars)
        
                
        
        