class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perm(nums, curr = []):
            if not nums:
                return [curr[:]]
            
            ret = []
            for i in range(len(nums)):
                ret.extend(perm(nums[:i] + nums[i + 1:],\
                                curr + [nums[i]]))
            
            return ret
        
        return perm(nums)
        
                
            
            
            