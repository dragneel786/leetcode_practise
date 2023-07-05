class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        fhalf = shalf = ans = 0
        zero = True
        for num in nums:
            if not num:
                zero = False
                ans = max(fhalf + shalf, ans)
                fhalf, shalf = shalf, 0
                continue
            
            shalf += 1
        
        return max(fhalf + shalf, ans) - zero