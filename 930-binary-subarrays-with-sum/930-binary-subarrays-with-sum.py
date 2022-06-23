class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def getSubArr(nums, s):
            res = j = 0
            for i in range(len(nums)):
                s -= nums[i]
                while(s < 0 and j <= i):
                    s += nums[j]
                    j += 1
                res += i - j + 1
            return res
                    
        
        return getSubArr(nums, goal) - getSubArr(nums, goal - 1)