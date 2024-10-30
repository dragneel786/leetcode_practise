class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lessers, greats = [1] * n, [1] * n
        for i in range(1, n - 1):
            val = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    val = max(lessers[j], val)
            
            lessers[i] += val
            
            val = 0
            for j in range(n - 1, n - i - 1, -1):
                if nums[j] < nums[n - i - 1]:
                    val = max(greats[j], val)
            
            greats[n - i - 1] += val
            
        
        min_del = inf
        for i in range(1, n - 1):
            if lessers[i] > 1 and greats[i] > 1:
                min_del = min(n - (greats[i] + lessers[i] - 1), min_del)
        
        return min_del
            
                
                
                    
            
            