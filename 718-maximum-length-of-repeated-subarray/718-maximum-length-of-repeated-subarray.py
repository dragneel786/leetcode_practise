class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1) + 1, len(nums2) + 1
        dp = [([0] * n2) for _ in range(n1)]
        
        max_so_far = 0
        for i in range(1, n1):
            for j in range(1, n2):
                if(nums1[i - 1] == nums2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_so_far = max(max_so_far, dp[i][j])
        
        return max_so_far
                    
        
        