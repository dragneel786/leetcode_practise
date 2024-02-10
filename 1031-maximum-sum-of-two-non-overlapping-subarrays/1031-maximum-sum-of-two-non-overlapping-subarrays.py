class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        @lru_cache(None)
        def find_max_sum(idx, f, s):
            if(f == s == 0 or idx >= len(nums)):
                return 0
            
            res = 0
            for i in range(idx, len(nums) - f - s + 1):
                sumation = (0 if not i else -nums[i - 1])
                if(f):
                    res = max(res, \
                              sumation + nums[i + f - 1] +\
                              find_max_sum(i + f, 0, s))
                else:
                    res = max(res, \
                              nums[i + s - 1] + sumation +\
                              find_max_sum(i + s, 0, 0))
            
            return res
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        val1 = find_max_sum(0, firstLen, secondLen)
        val2 = find_max_sum(0, secondLen, firstLen)
        # print(val1, val2)
        return max(val1, val2)
                              
            
            
            
                
            
        