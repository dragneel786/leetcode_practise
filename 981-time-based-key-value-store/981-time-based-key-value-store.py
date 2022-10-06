class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.time_map):
            return ""
        
        idx = bisect_right(self.time_map[key], (timestamp, "}"))
        
        if(idx < 1): return ""
        return self.time_map[key][idx - 1][1]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)