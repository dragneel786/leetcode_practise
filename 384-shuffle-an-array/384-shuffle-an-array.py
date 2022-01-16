import random
class Solution:
    original = list()
    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.original)
        curr = self.original[:]
        for i in range(n - 1, -1, -1):
            n -= 1
            r = random.randint(0, n)
            curr[i], curr[r] = curr[r], curr[i]
        
        return curr
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()