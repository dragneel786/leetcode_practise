class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [v for f, v in zip(nums[::2], nums[1::2]) for _ in range(f)]