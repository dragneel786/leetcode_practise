class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(not s): return 0
        
        uniq = Counter()
        max_len = left = 0
        
        for right in range(len(s)):
            c = s[right]
            
            if(uniq[c]):
                max_len = max(right - left, max_len)
                left = max(left, uniq[c])
            
            uniq[c] = right + 1
        
        return max(max_len, right - left + 1)
            
            