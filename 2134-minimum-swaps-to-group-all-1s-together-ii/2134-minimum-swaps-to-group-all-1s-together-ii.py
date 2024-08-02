class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        for num in nums:
            ones += (num == 1)
        
        nums.extend(nums[0: ones + 1])
        zeros = 0
        res = inf
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
                
            if i + 1 >= ones:
                if i >= ones:
                    zeros -= (nums[i - ones] == 0)
                res = min(res, zeros)
                
        return res
        
        
        
        
        
        
                
                