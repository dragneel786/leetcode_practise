class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        for i in range(1, n):
            steps[0], steps[1] = steps[1], steps[0] + steps[1]
        
        return steps[0]
        