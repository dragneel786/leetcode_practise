class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            po, inc = questions[i]
            idx = i + inc + 1
            val = dp[idx] if(idx < n) else 0
            dp[i] = max(dp[i + 1], val + po)
    
        return dp[0]


