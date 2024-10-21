class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def max_splits(idx, seen = set()):
            nonlocal s
            if idx >= len(s):
                return len(seen)
            
            ret = 0
            for i in range(idx, len(s)):
                if s[idx: i + 1] not in seen:
                    ret = max(ret, max_splits(i + 1, seen | {s[idx: i + 1]}))
            
            
            return ret
        
        
        return max_splits(0)
                    
                