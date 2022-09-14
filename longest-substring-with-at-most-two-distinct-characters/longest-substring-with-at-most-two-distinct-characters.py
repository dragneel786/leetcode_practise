class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i = 0
        hmap = Counter()
        
        for c in s:
            hmap[c] += 1
            
            if(len(hmap) > 2):
                hmap[s[i]] -= 1
                
                if(not hmap[s[i]]):
                    del hmap[s[i]]
                
                i += 1
            
        return len(s) - i
            
            