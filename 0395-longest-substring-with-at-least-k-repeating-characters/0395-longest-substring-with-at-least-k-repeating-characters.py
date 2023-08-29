class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for curr_unique in range(1, len(set(s)) + 1):
            chars = [0] * 26
            start = end = unique = count_at_k = 0
            while(end < n):
                
                if(unique <= curr_unique):
                    idx = ord(s[end]) - 97
                    if(chars[idx] == 0): unique += 1
                    chars[idx] += 1
                    if(chars[idx] == k): count_at_k += 1
                    end += 1
                
                else:
                    idx = ord(s[start]) - 97
                    if(chars[idx] == k): count_at_k -= 1
                    chars[idx] -= 1
                    if(chars[idx] == 0): unique -= 1
                    start += 1
                
                if(unique == curr_unique == count_at_k):
                    res = max(end - start, res)
        
        return res
                
                        