class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        bits = [0] * 32
        max_val = 0
        for c in candidates:
            start = 0
            while((1 << start) <= c):
                if((1 << start) & c):
                    bits[start] += 1
                
                max_val = max(bits[start], max_val)
                start += 1
        
        return max_val
                