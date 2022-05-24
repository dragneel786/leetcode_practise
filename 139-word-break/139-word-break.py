class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        seen = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if(dp[j + 1] and s[i:j + 1] in seen):
                    dp[i] = True
                    break
        return dp[0]