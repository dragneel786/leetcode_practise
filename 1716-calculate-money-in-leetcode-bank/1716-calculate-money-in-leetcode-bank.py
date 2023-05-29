class Solution:
    def totalMoney(self, n: int) -> int:
        mul = n // 7
        start = 1
        ans = 0
        for i in range(mul):
            sub = (start * (start - 1) // 2)
            end = start + 6
            ans += (end * (end + 1) // 2) - sub
            start += 1
        
        return ans + sum([mul + 1 + i for i in range(n % 7)])