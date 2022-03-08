class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumN = 0
        prodN = 1
        while(n):
            m = n % 10
            sumN += m
            prodN *= m
            n //= 10
        
        return prodN - sumN