class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        currDiff = 0
        prevDiff = float("-inf")
        count = 0
        res = 0
        for i in range(1, len(nums)):
            currDiff = nums[i - 1] - nums[i]
            if(currDiff == prevDiff):
                count += 1
            else:
                count = 1
                prevDiff = currDiff
            
            if(count > 1):
                res += (count - 1)
        return res