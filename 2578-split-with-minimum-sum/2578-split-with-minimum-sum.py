class Solution:
    def splitNum(self, num: int) -> int:
        num1 = 0
        num2 = 0
        bug = False
        num = str(num)
        for c in sorted(list(num)):
            if(bug):
                num1 = (num1 * 10) + int(c)
            else:
                num2 = (num2 * 10) + int(c)
            
            bug = not bug
        
        return num1 + num2