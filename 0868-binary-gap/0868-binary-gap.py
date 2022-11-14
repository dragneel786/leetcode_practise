class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = curr = 0
        prev = -1
        while(n):
            if(n & 1):
                if(prev != -1):
                    max_gap = max(curr - prev, max_gap)
                prev = curr
                
            n >>= 1
            curr += 1
        
        return max_gap