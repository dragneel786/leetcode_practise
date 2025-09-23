class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        num_set = set(nums)
        start = floor(sum(nums) / len(nums)) + 1
        if start <= 0: start = 1
        while(start in num_set):
            start += 1
        
        return start
        