class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True
        idx = [n]
        for i in range(n - 1, -1, -1):
            for j in idx:
                if(s[i: j] in wordDict):
                    dp[i] = True
                    idx.append(i)
                    break

        return dp[0]