class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float("inf")
        n = len(nums)
        sums = 0
        sumSize = 0
        j = 0
        for i in range(n):
            sums += nums[i]
            sumSize += 1
            while(j <= i and sums >= target):
                minSize = min(minSize, sumSize)
                sumSize -= 1
                sums -= nums[j]
                j += 1

        return minSize if minSize != float('inf') else 0