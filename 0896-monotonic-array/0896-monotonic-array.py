class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = None   
        for i in range(1, n):
            if(nums[i] == nums[i - 1]):
                continue
                
            if(inc is None):
                inc = nums[i - 1] < nums[i]
            
            elif((nums[i - 1] < nums[i]) != inc):
                return False
            
            print(inc)
        return True