class Solution:
    def minFlips(self, s: str) -> int:
        switch = lambda v: '0' if(v == '1') else '1'
        decrement = lambda pos, st, pre: (pre != st) if(pos >= n) else 0

        n = len(s)
        s += s
        flip1 = flip2 = 0
        start = prev = '0'
        min_flip = inf
        for i in range(2 * n):
            min_flip = min(flip1, flip2, min_flip) if(i >= n) else inf

            flip1 += (start != s[i]) - decrement(i, s[i - n], prev)
            flip2 += (start == s[i]) - decrement(i, s[i - n], switch(prev))

            prev = switch(prev) if(i >= n) else prev
            start = switch(start)

        return min_flip
            
            
        
            
            
    