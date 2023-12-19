class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @lru_cache(None)
        def get_max(start):
            if(start >= len(arr)):
                return 0
            
            ret_max = 0
            max_so_far = 0
            for i in range(start, min(start + k, len(arr))):
                max_so_far = max(max_so_far, arr[i])
                sub_sum = max_so_far * (i - start + 1)
                ret_max = max(ret_max, sub_sum + get_max(i + 1))
            
            return ret_max
        
        return get_max(0)
        
        
                
            
            