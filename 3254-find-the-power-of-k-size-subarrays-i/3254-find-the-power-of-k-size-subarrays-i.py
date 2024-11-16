class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        counts = Counter()
        si = 0
        res = []
        for i in range(1, len(nums)):
            counts[nums[i] - nums[i - 1]] += 1
            if i >= k:
                diff = nums[si + 1] - nums[si]
                counts[diff] -= 1
                if counts[diff] == 0: del counts[diff]
                si += 1
            
            if i >= k - 1:
                if 1 not in counts or counts[1] != k - 1:
                    res.append(-1)
                
                else:
                    res.append(nums[i])
    
        return res
            
            
                
        
        
        
        