class Solution:
    def check(self, nums: List[int]) -> bool:
        
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i + 1]):
                break
        else:
            return True
        
        v = -inf
        for num in nums[i + 1:] + nums[:i + 1]:
            if(v > num):
                return False
            v = num
        return True
            
            