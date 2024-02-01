class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = count = i = 0
        for num in nums:
            if num & 1:
                k -= 1
                count = 0
            
            while(not k):
                k += nums[i] & 1
                count += 1
                i += 1
            
            res += count
        
        return res
        
        
            
            
            
            