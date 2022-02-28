class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ranges = []
        nums.append(float('inf'))
        start = nums[0]
        for i in range(1, n + 1):
            if(nums[i] != nums[i - 1] + 1):
                if(start == nums[i - 1]):
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        
        return ranges