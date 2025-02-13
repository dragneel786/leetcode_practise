class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_val = 0
        for s in special:
            max_val = max(s - bottom, max_val)
            bottom = s + 1
        
        return max(max_val, top - bottom + 1)
