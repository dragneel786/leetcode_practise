class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avgset = set()
        n = len(nums) - 1
        for i in range(len(nums) // 2):
            avgset.add((nums[i] + nums[n - i]) / 2)
            
        return len(avgset)
        
        