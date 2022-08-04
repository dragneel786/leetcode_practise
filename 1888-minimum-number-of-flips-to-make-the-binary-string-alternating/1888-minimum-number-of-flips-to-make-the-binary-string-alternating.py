class Solution:
    def minFlips(self, s: str) -> int:
        switch = lambda v: '0' if(v == '1') else '1'
            
        n = len(s)
        s += s
        flip1 = flip2 = 0
        start = '0'
        
        for i in range(n):
            flip1 += (start != s[i])
            flip2 += (switch(start) != s[i])
            start = switch(start)
        
        prev = '0'
        temp_flip1 = flip1
        temp_flip2 = flip2
        for i in range(n - 1):
            temp_flip1 -= (prev != s[i])
            temp_flip2 -= (switch(prev) != s[i])
            
            temp_flip1 += (start != s[n + i])
            temp_flip2 += (switch(start) != s[n + i])
            
            flip1 = min(temp_flip1, flip1)
            flip2 = min(temp_flip2, flip2)
            
            prev = switch(prev)
            start = switch(start)
        
        return min(flip1, flip2)
            
            
        
            
            
    