class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.createSubset(nums, res)
        return res

    def createSubset(self, nums, res, op = []):
        if(not nums):
            if(op not in res):
                res.append(op)
            return

        self.createSubset(nums[1: ], res, op + [nums[0]])
        self.createSubset(nums[1: ], res, op)
    