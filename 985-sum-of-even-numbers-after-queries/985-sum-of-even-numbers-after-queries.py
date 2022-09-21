class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        res = []
        
        for num in nums:
            if(not num & 1):
                even_sum += num
        
        for val, index in queries:
            before, after = nums[index], nums[index] + val
            if(not before & 1):
                even_sum -= before
            
            if(not after & 1):
                even_sum += after
            
            nums[index] = after
            res.append(even_sum)
        
        return res
            
            
            
        
        
        