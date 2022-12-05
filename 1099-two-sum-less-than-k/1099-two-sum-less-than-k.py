class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = -1
        
        while(i < j):
            if(nums[i] + nums[j] >= k):
                j -= 1
            else:
                res = max(nums[i] + nums[j], res)
                i += 1
    
        return res
        