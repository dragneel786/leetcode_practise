class Solution:
    def numSub(self, s: str) -> int:
        MOD = (10 ** 9) + 7
        ans = ones = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                ones = 0
            
            ans = (ans + ones) % MOD

        return ans