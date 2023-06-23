class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = dict()
        n = len(nums)
        res = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                val = ans.get((diff, j), 1)
                ans[(diff, i)] = val + 1
                res = max(res, val + 1)
        return res
                
        
#         @lru_cache(None)
#         def series(i, prev = -1, diff = None):
#             if(i >= len(nums)):
#                 return 0
            
#             ans = 0
#             if(prev == -1 or diff == nums[i] - prev):
#                 ans = 1 + series(i + 1, nums[i], diff)
            
#             elif(diff is None):
#                 ans = 1 + series(i + 1, nums[i], nums[i] - prev)
            
#             return max(ans, series(i + 1, prev, diff))
            
        
#         return series(0)