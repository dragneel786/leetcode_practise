class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [([0] * 101) for _ in range(101)] 
        
        dp[0][0] = poured
        for i in range(100):
            for j in range(100):
                if(dp[i][j] >= 1):
                    dp[i + 1][j] += ((dp[i][j] - 1) / 2)
                    dp[i + 1][j + 1] += ((dp[i][j] - 1) / 2)
                    dp[i][j] = 1   
            
        return dp[query_row][query_glass]