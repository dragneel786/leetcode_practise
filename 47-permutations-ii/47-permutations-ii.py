class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def genPermute(nums, op = []):
            if(not nums):
                res.append(op)
                return
            
            for i in range(len(nums)):
                if(i == 0 or (i != 0 and nums[i] != nums[i - 1])):
                    genPermute(nums[:i] + nums[i + 1:], op + [nums[i]])
                    
        genPermute(nums)
        return res
        
        
        