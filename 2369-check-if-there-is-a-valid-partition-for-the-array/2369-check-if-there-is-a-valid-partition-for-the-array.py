class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def is_partition(i):
            if(i >= n):
                return True
            
            
            if(i < n - 1 and nums[i] == nums[i + 1]\
               and is_partition(i + 2)):
                return True
            
            if(i < n - 2):
                if(nums[i] == nums[i + 1] == nums[i + 2]):
                    return is_partition(i + 3)
                
                if(nums[i] + 2 == nums[i + 1] + 1 == nums[i + 2]):
                    return is_partition(i + 3)
            
            return False
        
        n = len(nums)
        return is_partition(0)
            