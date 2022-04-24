class UndergroundSystem:

    def __init__(self):
        self.customer = defaultdict(lambda:[])
        self.avg = defaultdict(lambda:[])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInTime = self.customer[id]
        self.avg[(checkInTime[0], stationName)]\
        .append(t - checkInTime[1])
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg = self.avg[(startStation, endStation)]
        return sum(avg) / len(avg)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)