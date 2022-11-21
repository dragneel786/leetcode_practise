class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seq = list(filter(lambda x: -x in set(nums), nums))
        return max(seq) if(len(seq)) else -1