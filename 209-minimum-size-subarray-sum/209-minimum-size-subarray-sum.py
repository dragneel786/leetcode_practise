class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        leng = float('inf')
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            while(j <= i and s >= target):
                leng = min(leng, (i - j + 1))
                s -= nums[j]
                j += 1
            
        return leng if(leng != float('inf')) else 0
            