class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        temp = [nums[0]]
        for i in nums:
            if(temp[-1] != i):
                temp.append(i)
        nums = temp
        n = len(nums)
        if(n == 1):
            return 1
        res = 2
        for i in range(1, len(nums) - 1):
            if(nums[i-1] < nums[i] and nums[i+1] < nums[i] or \
                nums[i-1] > nums[i] and nums[i+1] > nums[i]):
                res += 1

        return res