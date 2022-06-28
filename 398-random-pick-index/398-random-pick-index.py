class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(lambda:deque())
        for i,n in enumerate(nums):
            self.dic[n].append(i)

    def pick(self, target: int) -> int:
        d = self.dic
        i = d[target].popleft()
        d[target].append(i)
        return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)