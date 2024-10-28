class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = -1
        nums.sort()
        for i, num in enumerate(nums):
            counts = 1
            while(num ** 2 in seen):
                counts += 1
                num **= 2
            
            if counts > 1:
                max_count = max(counts, max_count)
                
            if max_count > len(nums) - i - 1:
                break
        
        return max_count
        
        