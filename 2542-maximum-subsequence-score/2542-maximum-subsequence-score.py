class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        values = [x for x in sorted(zip(nums2, nums1),
                                    reverse=True)]
        
        ans = 0
        sums = 0
        heap = []
        for i in range(len(values)):
            b, a = values[i]
            sums += a
            
            if(i >= k):
                sums -= heappop(heap)
            
            if(i >= k - 1):
                ans = max(sums * b, ans)
                
            heappush(heap, a)
            
        return ans
            
                
        
        