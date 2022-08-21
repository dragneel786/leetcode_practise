class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        stations.sort()
        reached = startFuel
        stops = 0
        index = 0
        
        while(reached < target):
            
            while(index < len(stations) and\
                  stations[index][0] <= reached):
                heappush(heap, -stations[index][1])
                index += 1
            
            if(not heap): return -1
            
            reached -= heappop(heap)
            stops += 1
        
        return stops
                
        
        
            
                
                