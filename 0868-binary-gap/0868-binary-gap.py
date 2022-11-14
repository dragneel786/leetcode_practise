class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        prev = curr = [0]
        while(n):
            if(n & 1):
                max_gap = max(curr[0] - prev[0], max_gap)
                prev = curr[:]
                
            n >>= 1
            curr[0] += 1
        
        return max_gap