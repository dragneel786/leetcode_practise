class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if(n == 0 or n == 1):
            return list(map(str, nums))
        
        ranges = []
        start = nums[0]
        end = nums[0]
        nums.append(float('inf'))
        for i in range(1, n + 1):
            if(nums[i] != end + 1):
                if(start == end):
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start = nums[i]
            end = nums[i]
        
        return ranges