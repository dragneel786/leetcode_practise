class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_val = 0
        for k in sorted(counts.keys()):
            if k + 1 in counts:
                max_val = max(counts[k] + counts[k + 1], max_val)
        
        return max_val 
