class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res = []
        while(num1 or num2 or num3):
            res.append(min(num1 % 10, num2 % 10, num3 % 10))
            num1 //= 10
            num2 //= 10
            num3 //= 10
        
        ans = 0
        for v in res[::-1]:
            ans = (ans * 10) + v
        return ans
            