class Solution:
        def getMoneyAmount(self, n: int) -> int:
            dp = [([0] * (n + 1)) for _ in range(n + 1)]

            for l in range(2, n + 1):
                maxStart = n - l + 1
                for s in range(1, maxStart + 1):
                    e = s + l - 1
                    tmp = float('inf')
                    for i in range(s, e + 1):
                        if(i == s):
                            tmp = min(tmp, i + dp[i + 1][e])
                        elif(i == e):
                            tmp = min(tmp, i + dp[s][i - 1])
                        else:
                            tmp = min(tmp, i + max(dp[s][i - 1], dp[i + 1][e]))
                    dp[s][e] = tmp
            
            return dp[1][n]