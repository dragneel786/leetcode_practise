class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xor_elements = lambda v: reduce(lambda a,b: a ^ b, v) if(v) else 0
        
        def subsets(nums, op = []):
            if(not nums): return xor_elements(op)
            
            return subsets(nums[1:], op + [nums[0]])\
        + subsets(nums[1:], op)
        
        return subsets(nums)
            