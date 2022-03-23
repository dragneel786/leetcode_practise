class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        if(target < startValue):
            return startValue - target
            
        while(target != startValue):
            if(target % 2 or target < startValue):
                target += 1
                steps += 1
            else:
                target //= 2
                steps += 1
        
        return steps
        
            