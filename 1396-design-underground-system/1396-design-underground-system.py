class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.stations = {}

        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, time = self.check[id]
        del self.check[id]
        
        self.stations[start_station] = self.stations\
        .get(start_station, {})
        time_count = self.stations[start_station]\
        .get(stationName, [0, 0])
        
        time_count[:] = [(t - time) + time_count[0],\
                         time_count[1] + 1]
        self.stations[start_station][stationName] = time_count

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot_time, count = self.stations[startStation][endStation]
        return tot_time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)