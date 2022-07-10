class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        j = 0
        long = 1
        minH = [(nums[0], 0)]
        maxH = [(-nums[0], 0)]
        nums.append(10 ** 9 + 9)
        for i in range(1, len(nums)):
            heappush(minH, (nums[i], i))
            heappush(maxH, (-nums[i], i))
            while(abs((-maxH[0][0]) - minH[0][0]) > limit and j < i):
                long = max(long, i - j)
                while(maxH[0][1] <= j):
                    heappop(maxH)
                while(minH[0][1] <= j):
                    heappop(minH)
                j += 1
        return max(long, i - j + 1)
                
            