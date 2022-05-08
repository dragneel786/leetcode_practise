class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(1, n):
            for j in range(n - i + 1):
                bisect.insort(res, sum(nums[j: j + i]))
        res.append(sum(nums))
        return sum(res[left - 1: right]) % (10 ** 9 + 7)