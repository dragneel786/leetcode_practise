class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        values = [[b, a] for a, b in zip(nums1, nums2)]
        values.sort(reverse=True)
        
        ans = 0
        sums = 0
        heap = []
        print(values)
        for i in range(len(values)):
            b, a = values[i]
            sums += a
            if(len(heap) >= k - 1):
                if(len(heap) == k):
                    sums -= heappop(heap)
                
                ans = max(sums * b, ans)
                
            heappush(heap, a)
            
        return ans
            
                
        
        