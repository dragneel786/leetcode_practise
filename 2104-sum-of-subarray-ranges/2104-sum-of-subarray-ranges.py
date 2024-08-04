class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        for start in range(len(nums)):
            min_val, max_val = inf, -inf
            for end in range(start, len(nums)):
                min_val = min(min_val, nums[end])
                max_val = max(max_val, nums[end])
                sums += (max_val - min_val)
        
        return sums
                
            
            
            