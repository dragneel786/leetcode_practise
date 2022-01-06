class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.genPermute(nums, res)
        return res

    def genPermute(self, nums, res, op = []):
        if(not nums):
            if(op not in res):
                res.append(op)
            return

        self.genPermute(nums[1:], res, op + [nums[0]])
        for i in range(1, len(nums)):
            if(nums[i] != nums[0] and nums[i] != nums[i - 1]):
                nums[0], nums[i] = nums[i], nums[0]
                self.genPermute(nums[1:], res, op + [nums[0]])
                nums[0], nums[i] = nums[i], nums[0]