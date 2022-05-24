class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        seen = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                print(s[i:j + 1])
                if(s[i:j + 1] in seen):
                    dp[i] = dp[j + 1]
                    if(dp[i]):
                        break
        return dp[0]