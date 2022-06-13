class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        dp = [([None] * cols) for _ in range(rows)]
        line = 0
        for r in range(rows):
            for c in range(cols):
                if(not mat[r][c]):
                    continue
                    
                dp[r][c] = {"h":1, "v":1, "d":1, "a":1}
                line = max(line, 1)
                if(r > 0 and mat[r - 1][c]):
                    dp[r][c]["v"] += dp[r - 1][c]["v"]
                    line = max(dp[r][c]["v"], line)
                    
                if(c > 0 and mat[r][c - 1]):
                    dp[r][c]["h"] += dp[r][c - 1]["h"]
                    line = max(dp[r][c]["h"], line)
                
                if(r > 0 and c > 0 and mat[r - 1][c - 1]):
                    dp[r][c]["d"] += dp[r - 1][c - 1]["d"]
                    line = max(dp[r][c]["d"], line)
                
                if(r > 0 and c < cols - 1 and mat[r - 1][c + 1]):
                    dp[r][c]["a"] += dp[r - 1][c + 1]["a"]
                    line = max(dp[r][c]["a"], line)
                
        return line