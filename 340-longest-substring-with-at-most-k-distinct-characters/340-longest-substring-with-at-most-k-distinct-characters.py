class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if(k == 0): 
            return 0
        
        j = 0
        uniq = Counter()
        longest = 0
        for i, c in enumerate(s + '*'):
            uniq[c] += 1
            longest = max(longest, i - j)
            
            while(len(uniq) > k):
                uniq[s[j]] -= 1
                if(not uniq[s[j]]):
                    del uniq[s[j]]
                j += 1
        
        return longest
        
        
        