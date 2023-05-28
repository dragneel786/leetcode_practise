class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @lru_cache(None)
        def min_weight(i, fhalf, shalf):
            nonlocal ans
            if(i == len(stones)):
                ans = min(abs(fhalf - shalf), ans)
                return
            
            min_weight(i + 1, fhalf + stones[i], shalf - stones[i])
            min_weight(i + 1, fhalf, shalf)
            
        
        ans = inf
        min_weight(0, 0, sum(stones))
        return ans
            
            
            