class Solution:
    def numSplits(self, s: str) -> int:
        count_distinct = lambda c: sum(1 for v in c.values() if(v))
        
        n = len(s)
        left = Counter()
        right = Counter(s)
        split_count = 0
        
        for c in s[:-1]:
            left[c] += 1
            right[c] -= 1
            if(count_distinct(left) == count_distinct(right)):
                split_count += 1
                
        return split_count
        
        
            
            
        