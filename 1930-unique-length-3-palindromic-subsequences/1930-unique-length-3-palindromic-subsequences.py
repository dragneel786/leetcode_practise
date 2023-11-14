class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        same_idx = defaultdict(list)
        for i, c in enumerate(s):
            sn = len(same_idx[c])
            if(sn < 2):
                same_idx[c].append(i)
            
            else:
                same_idx[c][1] = i
        
        
        counts = 0
        for indexes in same_idx.values():
            sn = len(indexes)
            if(sn < 2):
                continue
            
            a, b = indexes
            counts += len(set(s[a + 1: b]))
        
        return counts
            
                
            