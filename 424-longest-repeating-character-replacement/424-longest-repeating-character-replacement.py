class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        chars[s[0]] += 1
        
        maxFreq = 1
        maxLen = k
        l = 0
        for r in range(1, len(s)):
            chars[s[r]] += 1
            maxFreq = max(chars[s[r]], maxFreq)
            if((r - l + 1) - maxFreq <= k):
                maxLen = max(maxLen, (r - l + 1))
            else:
                chars[s[l]] -= 1
                l += 1
        return maxLen
                