class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def numOfOne(val):
            ones = 0
            while(val):
                val &= val - 1
                ones += 1
            return ones
        
        if(start > goal): return self.minBitFlips(goal, start)
        count = 0
        while(start > 0 and goal > 0):
            count += start & 1 != goal & 1
            start, goal = start >> 1, goal >> 1
        return count + numOfOne(goal)