class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = left = 0
        max_freq = 0
        for right in range(len(nums)):
            s += nums[right]
            while(left < right and (nums[right] *\
                                    (right - left + 1)) > s + k):
                s -= nums[left]
                left += 1
            
            max_freq = max((right - left + 1), max_freq)
        
        return max_freq
                
            
                
        