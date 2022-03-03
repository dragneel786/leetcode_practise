class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0
        prev = float('inf')
        for i in range(1,n):
            diff = nums[i - 1] - nums[i]
            if(diff == prev):
                count += 1
            else:
                count = 1
                prev = diff
            
            if(count > 1):
                res += (count - 1)
                
        return res
        