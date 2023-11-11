class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        remain = set([i for i in range(1, k + 1)])
        for _ in range(len(nums)):
            remain.discard(nums.pop())
            if(len(remain) == 0):
                return _ + 1
        