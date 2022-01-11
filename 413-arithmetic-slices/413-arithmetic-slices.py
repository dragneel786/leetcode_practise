class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        currCount = 0
        currDiff = 0
        prevDiff = float('-inf')
        res = 0
        for i in range(1, len(nums)):
            currDiff = nums[i] - nums[i - 1]
            if(currDiff == prevDiff):
                currCount += 1
            else:
                currCount = 1
                prevDiff = currDiff

            if(currCount > 1):
                res += (currCount - 1)

        return res