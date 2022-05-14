class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(lambda:[])

    def set(self, key: str, value: str, timestamp: int) -> None:
        insort(self.timeMap[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.timeMap[key], (timestamp, "z" * 101))
        return self.timeMap[key][idx - 1][1] if idx else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)