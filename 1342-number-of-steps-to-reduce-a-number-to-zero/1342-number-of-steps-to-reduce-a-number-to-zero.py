class Solution:
    def numberOfSteps(self, num: int) -> int:
        if(not num):
            return 0
        steps = 0
        while(num):
            if(num & 1):
                steps += 1
            num >>= 1
            steps += 1
        return steps - 1