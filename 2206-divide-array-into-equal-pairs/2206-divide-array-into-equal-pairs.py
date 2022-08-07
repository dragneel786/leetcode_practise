class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        C = Counter(nums)
        return all(v % 2 == 0 for v in C.values())
        