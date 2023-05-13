class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)
        cn = (n + k - 1)
        complete = (cn * (cn + 1)) // 2
        half = ((n - 1) * n) // 2
        return complete - half
        