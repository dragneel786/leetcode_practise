class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        min_idx = 0
        for i in range(len(nums)):
            if(nums[min_idx] > nums[i]):
                min_idx = i
                
            if(nums[i] >= 0 or not k):
                break
                
            nums[i] *= -1
            k -= 1
        
        k %= 2
        if(k):
            nums[min_idx] *= -1
        
        return sum(nums)
            
            