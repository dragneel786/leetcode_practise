class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        
        if num % 9 == 0:
            return 9
        
        return num % 9