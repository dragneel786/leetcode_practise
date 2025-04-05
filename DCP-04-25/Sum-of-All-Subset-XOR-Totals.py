class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subset_form(idx, xor):
            nonlocal tot
            if idx >= len(nums):
                tot += xor
                return

            subset_form(idx + 1, xor)
            subset_form(idx + 1, xor ^ nums[idx])

        tot = 0
        subset_form(0, 0)
        return tot
