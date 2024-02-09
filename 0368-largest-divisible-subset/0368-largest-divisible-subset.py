class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        s = {-1: set()}
        for num in sorted(nums):
            s[num] = max([s[d] for d in s if num % d == 0], key=len) | {num}
        return max(s.values(), key=len)
        
        