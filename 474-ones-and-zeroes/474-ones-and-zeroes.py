class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def freqCounts(st):
            ones = 0
            zeros = 0
            for s in st:
                if(s == '1'):
                    ones += 1
                else:
                    zeros += 1
            return [zeros, ones]
        
        freq = [freqCounts(strs[i]) for i in range(len(strs))]
        dp = [([0] * (m + 1))for _ in range(n + 1)]

        for k in range(len(strs)):
            zeros = freq[k][0]
            ones = freq[k][1]

            for i in range(n, ones - 1, -1):
                for j in range(m, zeros - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeros] + 1)

        return dp[n][m]