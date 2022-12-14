class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_it(idx):
            if(idx >= len(nums)):
                return 0
            
            if(idx in memo):
                return memo[idx]
            
            memo[idx] = max(rob_it(idx + 2) + nums[idx], rob_it(idx + 1))
            return memo[idx]
        
        memo = dict()
        return max(rob_it(0), rob_it(1))