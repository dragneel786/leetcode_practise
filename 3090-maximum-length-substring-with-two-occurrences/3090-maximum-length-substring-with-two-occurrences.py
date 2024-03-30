class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = Counter()
        ans = start = 0
        for end in range(len(s)):
            counts[s[end]] += 1
            while(counts[s[end]] > 2):
                counts[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
        
        return ans
            