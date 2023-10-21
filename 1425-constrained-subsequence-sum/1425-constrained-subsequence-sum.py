class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [0] * n
        res = -inf
        heap = []
        for i, num in enumerate(nums):
            dp[i] = num
            while(heap and (i - heap[0][1]) > k):
                heappop(heap)
            
            if(heap):
                dp[i] = max(dp[i], dp[i] + -heap[0][0])
            
            res = max(dp[i], res)
            heappush(heap, (-dp[i], i))
        
        return res
            
            
        
        
            