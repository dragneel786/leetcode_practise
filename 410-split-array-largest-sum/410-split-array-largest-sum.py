class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        low = float('-inf')
        high = 0
        for i in range(n):
            low = max(low, nums[i])
            high += nums[i]

        ans = 0
        while(low <= high):
            tillSum = 0
            split = 1
            mid = low + (high - low) // 2
            for i in range(n):
                if(tillSum + nums[i] > mid):
                    tillSum = 0
                    split += 1
                tillSum += nums[i]

            if(split <= m):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans if ans else max(nums)

   
    

