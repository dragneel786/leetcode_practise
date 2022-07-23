class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorte = []
        res = deque()
        for i in range(len(nums) - 1, -1, -1):
            idx = bisect_left(sorte, nums[i])
            res.appendleft(idx)
            insort(sorte, nums[i])
        return res