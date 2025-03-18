class Solution:
    def maxSum(self, nums: List[int]) -> int:
        counts, res = Counter(nums), 0
        for k in counts.keys():
            if k > 0:
                res += k

        if res > 0:
            return res
        
        return max(counts.keys())

