class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        values = set(nums)
        seq = list(filter(lambda x: -x in values, nums))
        return max(seq) if(len(seq)) else -1