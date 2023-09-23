class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        n = len(words)
        dp = Counter()
        max_overall = 0
        for word in words:
            max_val = 1
            for i in range(len(word)):
                term = word[:i] + word[i + 1:]
                max_val = max(max_val, dp[term] + 1)
        
            dp[word] = max_val
            max_overall = max(max_val, max_overall)
        
        return max_overall