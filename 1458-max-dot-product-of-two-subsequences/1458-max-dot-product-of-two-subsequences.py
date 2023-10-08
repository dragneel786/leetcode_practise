class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        n1, n2 = len(nums1), len(nums2)
        dp = [([0] * (n2 + 1)) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(prod + dp[i - 1][j - 1],\
                               dp[i][j - 1], dp[i - 1][j])
        return dp[n1][n2]
        
#         @lru_cache(None)
#         def max_res(i, j, choosen = False):
#             if(i >= len(nums1) or j >= len(nums2)):
#                 return 0 if(choosen) else -inf
            
#             res = max_res(i + 1, j, choosen)
#             for k in range(j, len(nums2)):
#                 prod = nums1[i] * nums2[k]
#                 res = max(prod + max_res(i + 1, k + 1, True), res)
                
#             return res
        
#         return max_res(0, 0)
        