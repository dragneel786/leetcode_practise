class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = []
        curr_sum = 0
        res = inf
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum >= k:
                res = min(res, i + 1)
                
            while(heap and curr_sum - heap[0][0] >= k):
                res = min(res, i - heappop(heap)[1])
            
            heappush(heap, [curr_sum, i])
        
        return res if res != inf else -1
            
            