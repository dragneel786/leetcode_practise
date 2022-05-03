class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        maxV = nums[0]
        end = -1
        for i in range(1, len(nums)):
            if(maxV > nums[i]):
                end = i
            else:
                maxV = nums[i]
                
        minV = nums[-1]
        start = -1
        for i in range(len(nums) - 1, -1, -1):
            if(minV < nums[i]):
                start = i
            else:
                minV = nums[i]
        val = end - start
        print(start, end)
        return val + 1 if(val) else 0
                