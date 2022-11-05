class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        prev_shot = timeSeries[0]
        poisoned_till = prev_shot + duration - 1
        total_time = 0
        
        for shot in timeSeries[1:]:
            if(shot > poisoned_till):
                total_time += (poisoned_till - prev_shot + 1)
                prev_shot = shot
                
            poisoned_till = shot + duration - 1
                
        return total_time + (poisoned_till - prev_shot + 1)
                
                
        