class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        values = [(e, s) for s, e in zip(speed, efficiency)]
        values.sort(reverse=True)
        
        heap = []
        run_sum = 0
        maxi = 0
        M = (10 ** 9) + 7
        
        for e, s in values:
            run_sum = (run_sum + s)
            heappush(heap, s)
            
            if(len(heap) > k):
                run_sum -= heappop(heap)
            
            maxi = max(maxi, (run_sum * e))
        
        return maxi % M
            
                
            
        
    
            