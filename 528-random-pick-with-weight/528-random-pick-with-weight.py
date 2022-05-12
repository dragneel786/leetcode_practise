class Solution:

    def __init__(self, w: List[int]):
        self.p = list(accumulate(w))
        
    def pickIndex(self) -> int:
        return bisect_left(self.p, random.random() * self.p[-1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()