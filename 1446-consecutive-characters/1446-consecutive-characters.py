class Solution:
    def maxPower(self, s: str) -> int:
        max_count = count = 1
        for i in range(1, len(s)):
            if(s[i] != s[i - 1]):
                max_count = max(count, max_count)
                count = 0
            count += 1
        
        return max(max_count, count)
                