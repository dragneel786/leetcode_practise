class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        s = 0
        left = 0
        maxL = 0
        for right in range(n):
            s += nums[right]
            while(left < right and (nums[right] * (right - left + 1) > s + k)):
                s -= nums[left]
                left += 1
            
            maxL = max(maxL, (right - left) + 1)
        
        return maxL