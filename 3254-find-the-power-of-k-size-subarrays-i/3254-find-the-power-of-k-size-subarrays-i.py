class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        counts = 0
        si = 0
        res = []
        for i in range(1, len(nums)):
            counts += (nums[i] - nums[i - 1] == 1)
            
            if i >= k:
                counts -= (nums[si + 1] - nums[si] == 1)
                si += 1
            
            if i >= k - 1:
                res.append(-1 if counts != k - 1 else nums[i])
    
        return res
            
            
                
        
        
        
        