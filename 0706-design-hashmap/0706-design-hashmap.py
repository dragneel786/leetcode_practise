class MyHashMap:

    def __init__(self):
        self.imap = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.imap[key] = value

    def get(self, key: int) -> int:
        return self.imap[key]

    def remove(self, key: int) -> None:
        self.imap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)