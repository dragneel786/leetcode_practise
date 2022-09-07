class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = Counter()
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            uniq[c] += 1
            
            while(uniq[c] > 1):
                uniq[s[left]] -= 1
                left += 1
            
            max_len = max(right - left + 1, max_len)
        
        return max_len
            
            