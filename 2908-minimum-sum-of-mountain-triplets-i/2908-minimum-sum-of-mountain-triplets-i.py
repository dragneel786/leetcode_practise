class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = inf
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:], i + 1):
                for c in nums[j + 1:]:
                    # print(a, b, c)
                    if(a < b > c):
                        # print(a, b, c)
                        res = min(a + b + c, res)
        
        return -1 if(res == inf) else res