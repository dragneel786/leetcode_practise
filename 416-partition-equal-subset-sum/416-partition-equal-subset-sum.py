class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def partitionIt(index, half):
            if(half <= 0 or index >= len(nums)):
                return half == 0
            
            key = (index, half)
            
            if(key in memo):
                return memo[key]
            
            memo[key] = partitionIt(index + 1, half - nums[index]) or \
        partitionIt(index + 1, half)
            
            return memo[key]
        
        total = sum(nums)
        if(total & 1): return False
        
        half = total // 2
        memo = {}
        return partitionIt(0, half)