class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n > 0 and n % 3 != 2):
            n = n // 3 if(n % 3 != 1) else n - 1
        return n == 0