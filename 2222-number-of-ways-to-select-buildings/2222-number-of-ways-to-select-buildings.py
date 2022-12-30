class Solution:
    def numberOfWays(self, s: str) -> int:
        
        zero1 = one0 = 0
        t1 = t0 = 0
        ans = 0
        for c in s:
            if(c == '0'):
                ans += zero1
                t0 += 1
                one0 += t1
            else:
                ans += one0
                t1 += 1
                zero1 += t0
            
        return ans
                