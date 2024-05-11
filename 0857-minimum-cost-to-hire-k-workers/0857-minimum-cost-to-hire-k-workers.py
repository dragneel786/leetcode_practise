class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio_qly = []
        for w, q in zip(wage, quality):
            ratio_qly.append([w/q, q])
        ratio_qly.sort()
        
        heap = []
        quality_sum = 0
        ans = inf
        for ratio, q in ratio_qly:
            quality_sum += q
            heappush(heap, -q)
            if len(heap) > k: quality_sum -= (-heappop(heap)) 
            if len(heap) == k: ans = min(ans, quality_sum * ratio)
            
        return ans
            
            
        
        
        
        