class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(lambda:[])
        for i,n in enumerate(nums):
            self.dic[n].append(i)

    def pick(self, target: int) -> int:
        li = self.dic[target]
        return random.choice(li)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)