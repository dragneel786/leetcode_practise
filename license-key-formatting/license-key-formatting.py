class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        temp = ''
        for c in s[::-1]:
            if(c == '-'):
                continue
                
            temp = c.upper() + temp

            if(len(temp) == k):
                res.append(temp)
                temp = ''
        
        if(temp): res.append(temp)
        return '-'.join(res[::-1]) 