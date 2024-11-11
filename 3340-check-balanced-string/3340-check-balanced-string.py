class Solution:
    def isBalanced(self, num: str) -> bool:
        val1 = val2 = 0
        change = True
        num = list(num)
        while(num):
            if change:
                val1 += int(num.pop())
            else:
                val2 += int(num.pop())
            
            change = not change
        
        return val1 == val2