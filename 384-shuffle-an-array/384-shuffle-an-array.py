import random
class Solution:
    original = list()
    curr = list()
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.curr = nums[:]

    def reset(self) -> List[int]:
        self.curr = self.original[:]
        return self.curr

    def shuffle(self) -> List[int]:
        n = len(self.curr)
        for i in range(n - 1, -1, -1):
            r = random.randint(0, n - 1)
            self.curr[i], self.curr[r] = self.curr[r], self.curr[i]
            n -= 1
        
        return self.curr
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()