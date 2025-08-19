class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        for l, r, k, v in queries:
            while(l < r + 1):
                nums[l] = ((nums[l] * v) % MOD)
                l += k
        
        return reduce(lambda x, y: x ^ y, nums)