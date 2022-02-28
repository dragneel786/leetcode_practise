class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if(n == 0 or n == 1):
            return list(map(str, nums))
        
        ranges = []
        start = nums[0]
        nums.append(float('inf'))
        for i in range(1, n + 1):
            if(nums[i] != nums[i - 1] + 1):
                if(start == nums[i - 1]):
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        
        return ranges