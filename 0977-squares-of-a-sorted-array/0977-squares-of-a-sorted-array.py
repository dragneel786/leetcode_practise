class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if(nums[i] >= 0):
                break
        
        pos_idx = i
        neg_idx = i - 1
        res = []
        while(pos_idx < n or neg_idx > -1):
            if((neg_idx <= -1) or \
               (pos_idx < n and nums[pos_idx] <= abs(nums[neg_idx]))):
                res.append(nums[pos_idx] ** 2)
                pos_idx += 1
            
            else:
                res.append(nums[neg_idx] ** 2)
                neg_idx -= 1
        
        return res
              
             
               