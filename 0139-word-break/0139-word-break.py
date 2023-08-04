class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i + 1):
                if(s[j:i + 1] in word_set and dp[j]):
                    dp[i + 1] = True
                    break
        
        return dp[n]