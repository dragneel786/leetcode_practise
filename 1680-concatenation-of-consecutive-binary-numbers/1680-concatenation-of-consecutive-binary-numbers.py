class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        size = 1
        for i in range(2, n + 1):
            log_value = log(i, 2)
            size += (ceil(log_value) == floor(log_value))
            res = ((res << size) + i) % MOD
        
        return res