class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        def create_counts():
            values = Counter()
            for i, c in enumerate(candidates):
                idx = 0
                while(c):
                    if c & 1:
                        values[idx] += 1
                     
                    c >>= 1
                    idx += 1
            
            return values
                
            
        idx_map = create_counts()
        cn = len(candidates)
        max_val = 0
        for v in idx_map.values():
            max_val = max(max_val, v)
            
        return max_val