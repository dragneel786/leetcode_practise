class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counts = 0
        ans = 0
        for num in nums:
            if(not num):
                counts += 1
            else:
                counts = 0
            
            ans += counts
        
        return ans