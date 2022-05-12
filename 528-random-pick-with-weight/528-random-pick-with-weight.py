class Solution:

    def __init__(self, w: List[int]):
        self.prefix = w
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i - 1]

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, random.random() * self.prefix[-1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()