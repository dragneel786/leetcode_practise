class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        C = Counter(nums)
        for v in C.values():
            if(v & 1):
                return False
        return True
        