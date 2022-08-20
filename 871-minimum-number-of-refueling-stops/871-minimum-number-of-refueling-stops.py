class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        refueling_options = []
        curr_station = refueling_stops = 0
        reachable_distance = startFuel
        while reachable_distance < target:
            while curr_station < len(stations) and stations[curr_station][0] <= reachable_distance:
                heapq.heappush(refueling_options, -stations[curr_station][1])
                curr_station += 1
            if not refueling_options: return -1
            reachable_distance += -heapq.heappop(refueling_options)
            refueling_stops += 1
        return refueling_stops
            
                
                