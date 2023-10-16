class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for _ in range(rowIndex):
            temp = [1]
            for i in range(1, len(dp)):
                temp.append(dp[i - 1] + dp[i])
            temp.append(1)
            
            dp = temp
        
        return dp