class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-math.inf] * n
        dp[0] = nums[0]
        heap = [(-nums[0], 0)]
        for i in range(1, n):
            while(len(heap) > k and heap[0][1] < (i - k)):
                heappop(heap)
            dp[i] = nums[i] + -heap[0][0]
            heappush(heap, (-dp[i], i))
        return dp[n - 1]
    