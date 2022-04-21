class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.arr = [False] * (10 ** 6 + 1)
        
    def add(self, key: int) -> None:
        self.arr[key % ((10 ** 6 + 1))] = True

    def remove(self, key: int) -> None:
        if(self.arr[key % ((10 ** 6 + 1))]):
            self.arr[key % ((10 ** 6 + 1))] = False
            return key
        

    def contains(self, key: int) -> bool:
        return self.arr[key % ((10 ** 6 + 1))]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)