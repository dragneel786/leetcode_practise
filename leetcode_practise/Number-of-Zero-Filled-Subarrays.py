class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        start = -1
        nums.append(1)
        for i, num in enumerate(nums):
            if num != 0:
                diff = (i - start - 1)
                ans += (diff * (diff + 1)) // 2
                start = i
            
        return ans
            
            

