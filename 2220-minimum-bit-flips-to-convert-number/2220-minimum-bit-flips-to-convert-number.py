class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while(start or goal):
            flips += not ((1 & start) == (1 & goal))
            if start: start >>= 1
            if goal: goal >>= 1
            
        return flips