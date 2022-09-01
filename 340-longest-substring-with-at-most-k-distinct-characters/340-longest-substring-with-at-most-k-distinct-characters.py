class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if(k == 0 or len(s) == 0):
            return 0
        
        hmap = OrderedDict()
        left = longest = 0
        for right, c in enumerate(s):
            if(c in hmap):
                del hmap[c]
            
            hmap[c] = right
            
            if(len(hmap) > k):
                _, idx = hmap.popitem(last = False)
                left = idx + 1
            
            longest = max(longest, right - left + 1)
        
        return longest
                
            
        
        
        
        