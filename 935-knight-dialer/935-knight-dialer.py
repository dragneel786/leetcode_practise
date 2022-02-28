class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        look = [[4, 6], [8, 6], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        for i in range(n - 1):
            temp = [0] * 10
            for i in range(10):
                for idx in look[i]:
                    temp[i] += dp[idx]
                
            dp = temp[:]
        
        return sum(dp) % (10 ** 9 + 7)