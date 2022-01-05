class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        self.addSubset(nums, res)
        return res

    def addSubset(self, nums, res, op = []):
        if(not nums):
            if(op not in res):
                res.append(op)
            return

        for i in range(len(nums)):
            self.addSubset(nums[i + 1: ], res, op)
            self.addSubset(nums[i + 1: ], res, op + [nums[i]])