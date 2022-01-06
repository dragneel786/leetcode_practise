class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = nums + [11]
        nums.sort()
        self.genPermute(nums, res)
        return res

    def genPermute(self, nums, res, op = []):
        if(len(nums) == 1):
            res.append(op)
            return

        for i in range(0, len(nums) - 1):
            if(nums[i] != nums[i - 1]):
                self.genPermute(nums[0: i] + nums[i + 1: ], res, op + [nums[i]])
            