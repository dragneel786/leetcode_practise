class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        maxReach = 0
        for i in range(len(nums)):
            if(not nums[i]):
                if(k == 0):
                    while(nums[j]):
                        j += 1
                    j += 1
                    k += 1
                k -= 1
            maxReach = max(maxReach, i - j + 1)
        return maxReach