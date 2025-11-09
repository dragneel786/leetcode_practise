class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 < num2:
            num1, num2 = num2, num1
        
        steps = 0
        while(num1 != 0 and num2 != 0):
            num1 -= num2
            if num1 < num2:
                num1, num2 = num2, num1
            
            steps += 1
        
        return steps
