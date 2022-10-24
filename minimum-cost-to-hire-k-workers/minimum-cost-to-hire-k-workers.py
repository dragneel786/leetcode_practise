class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        from fractions import Fraction
        
        combos = sorted((w / q, q, w)\
                        for w, q in zip(wage, quality))
        sumq = 0
        heap = []
        ans = inf
        
        for ratio, q, w in combos:
            heappush(heap, -q)
            sumq += q
            
            if(len(heap) > k):
                sumq += heappop(heap)
            
            if(len(heap) == k):
                ans = min(ans, sumq * ratio)
    
        return ans
                    
                
        
        
        