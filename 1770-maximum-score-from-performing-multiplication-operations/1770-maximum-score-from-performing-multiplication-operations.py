class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left]\
                                   + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)]\
                                   + dp[op + 1][left])

        return dp[0][0]
        
#         def max_score(start, i):
#             if(i == len(multipliers)):
#                 return 0
            
#             key = (start, i)
#             if(key in memo): return memo[key]
            
#             end = len(nums) - (i - start + 1)
            
#             sval = nums[start] * multipliers[i]
#             enval = nums[end] * multipliers[i]
            
#             memo[key] = max(sval + max_score(start + 1, i + 1),\
#                        enval + max_score(start, i + 1))
            
#             return memo[key]
        
#         memo = dict()
#         return max_score(0, 0)