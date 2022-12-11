class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        return max((v for v, c in Counter(nums).items() if(c == 1)))