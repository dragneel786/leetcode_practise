class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        size = 1
        for i in range(2, n + 1):
            size += (i & (i - 1) == 0)
            res = ((res << size) | i) % MOD
        
        return res