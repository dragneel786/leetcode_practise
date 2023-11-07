class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        atm_time = []
        for d, s in zip(dist, speed):
            atm_time.append((d / s) if(d >= s) else 0)
        
        atm_time.sort()
        counts = 1
        time = 1
        for a in atm_time[1:]:
            if(a <= time):
                break
                
            counts += 1
            time += 1
        
        return counts
            
                
            