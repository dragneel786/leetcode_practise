class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            a = 2 * dp[p2]
            b = 3 * dp[p3]
            c = 5 * dp[p5]
            res = min(a, min(b, c))
            if(res == a):
                p2 += 1
            if(res == b):
                p3 += 1
            if(res == c):
                p5 += 1
            dp[i] = res

        return dp[n]
