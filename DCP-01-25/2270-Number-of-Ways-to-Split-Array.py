class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tot = sum(nums)
        curr = splits = 0
        for num in nums[:-1]:
            curr += num
            tot -= num

            if curr >= tot:
                splits += 1
            

        return splits
            

