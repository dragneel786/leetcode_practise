class MRUQueue:

    def __init__(self, n: int):
        self.q = [i for i in range(1, n + 1)]
        
    def fetch(self, k: int) -> int:
        v = self.q.pop(k - 1)
        self.q.append(v)
        return v


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)