class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n:
            return -1
        
        ans = 0
        while(n):
            if n & 1 != k & 1:
                if n & 1 == 0:
                    return -1
                
                ans += 1
            
            if n: n >>= 1
            if k: k >>= 1
        
        return ans