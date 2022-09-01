class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if(k == 0): 
            return 0
        
        def update(uniq, start):
            for idx, ch in enumerate(s[start: i]):
                uniq[ch] -= 1
                if(not uniq[ch]):
                    del uniq[ch]
                
                if(len(uniq) == k):
                    return idx + 1
            
            return idx + 1
        
        
        j = 0
        uniq = Counter()
        longest = 0
        for i, c in enumerate(s + '*'):
            uniq[c] += 1
            longest = max(longest, i - j)
            
            if(len(uniq) > k):
                j += update(uniq, j)
        
        return longest
        
        
        