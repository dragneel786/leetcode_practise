class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for v in counts.values():
            if v % 2 == 1:
                return False
        
        return True