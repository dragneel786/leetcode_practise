class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:   
        n = len(nums)
        pref_max = [0] * n
        pref_max[0] = nums[0]
        suff_max = [0] * n
        suff_max[-1] = nums[-1]
        for i in range(1, n):
            pref_max[i] = max(nums[i], pref_max[i - 1])
            suff_max[n - i - 1] = max(nums[n - i - 1], suff_max[n - i])

        res = 0
        for j in range(1, n - 1):
            res = max(res, (pref_max[j - 1] - nums[j]) * suff_max[j + 1])

        return res

