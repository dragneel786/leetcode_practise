class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        total_time = 0
        for i, shot in enumerate(timeSeries[:-1], 1):
            total_time += min(timeSeries[i]\
                              - timeSeries[i - 1], duration)
            
                
        return total_time + duration
                
                
        