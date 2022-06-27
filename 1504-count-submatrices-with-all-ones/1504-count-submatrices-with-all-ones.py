class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [([0] * n) for _ in range(m)]
        for r in range(m):
            t = 0
            for c in range(n - 1, -1, -1):
                t = t + 1 if(mat[r][c]) else 0
                dp[r][c] = t
        
        ans = 0
        for r in range(m):
            for c in range(n):
                v = math.inf
                for k in range(r, m):
                    v = min(v, dp[k][c])
                    ans += v
        return ans