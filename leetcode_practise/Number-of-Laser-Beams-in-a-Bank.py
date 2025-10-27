class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = prev_counts = 0
        for b in bank:
            counts = b.count("1")
            if counts > 0:
                res += counts * prev_counts
            
            if counts > 0:
                prev_counts = counts
        
        return res
        