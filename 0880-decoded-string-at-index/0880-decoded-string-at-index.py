class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        chr_count = 0
        for i, c in enumerate(s):
            if(c.isdigit()):
                chr_count *= int(c)
            else:
                chr_count += 1
                
            if(chr_count >= k):
                break
        
        for j in range(i, -1, -1):
            c = s[j]
            if(c.isdigit()):
                chr_count //= int(c)
                k %= chr_count
            
            else:
                if(k == chr_count or k == 0):
                    return c
                chr_count -= 1
        
                
        
        
                
            
            
                
                
                
            