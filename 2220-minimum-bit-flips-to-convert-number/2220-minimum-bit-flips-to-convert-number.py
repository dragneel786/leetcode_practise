class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if(start > goal): return self.minBitFlips(goal, start)
        
        count = 0
        while(start > 0 or goal > 0):
            if(start & 1 != goal & 1):
                count += 1
            start, goal = start >> 1, goal >> 1
        return count