class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = nums[:]
        for i in range(1, n):
            nums[i] += nums[i - 1]
            
        for i in range(2, n):
            res.append(nums[i - 1])
            for j in range(1, n - i + 1):
                res.append(nums[j + i - 1] - nums[j - 1])
        res.sort()
        res.append(nums[-1])
        # print(res)
        return sum(res[left - 1: right]) % (10 ** 9 + 7)