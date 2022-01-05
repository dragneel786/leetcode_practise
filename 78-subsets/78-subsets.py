class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        self.addSubset(nums, res)
        return res

    def addSubset(self, nums, res, op = []):
        if(not nums):
            res.append(op)
            return

        self.addSubset(nums[1: ], res, op)
        self.addSubset(nums[1: ], res, op + [nums[0]])