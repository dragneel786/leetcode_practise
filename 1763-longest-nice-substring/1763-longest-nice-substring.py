class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def is_nice(c):
            for k in c.keys():
                if(k.isupper() and not c[k.lower()]):
                    return False
                if(k.islower() and not c[k.upper()]):
                    return False
            return True
                
                
        n = len(s)
        for w in range(n, 0, -1):
            c = Counter(s[0: w])
            
            if(is_nice(c)):
                return s[0: w]
            
            for j in range(1, n - w + 1):
                c[s[j - 1]] -= 1
                if(not c[s[j - 1]]): c.pop(s[j - 1])
                c[s[j + w - 1]] += 1
                
                if(is_nice(c)):
                    return s[j: j + w]
        return ""