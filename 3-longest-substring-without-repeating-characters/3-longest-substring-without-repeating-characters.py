class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda:0)
        j = 0
        n = len(s)
        long = 0
        for i in range(n):
            seen[s[i]] += 1
            while(j <= i and seen[s[i]] > 1):
                seen[s[j]] -= 1
                j += 1
            
            long = max(long, i - j + 1)
        
        return long