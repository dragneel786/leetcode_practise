class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def partitionIt(index, val = 0):
            nonlocal total
            if(len(nums) == index):
                return val == (total - val)
            
            key = (index, val)
            
            if(key in memo):
                return memo[key]
            
            memo[key] = partitionIt(index + 1, val + nums[index]) or \
        partitionIt(index + 1, val)
            
            return memo[key]
        
        total = sum(nums)
        if(total & 1): return False
        
        memo = {}
        return partitionIt(0)