class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def numOfOne(val):
            ones = 0
            while(val):
                val &= val - 1
                ones += 1
            return ones
        
        return numOfOne(start ^ goal)