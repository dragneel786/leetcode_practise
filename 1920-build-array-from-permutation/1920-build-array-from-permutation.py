class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            val = nums[nums[i]] % n
            nums[i] = (val * n) + nums[i]
        
        for i in range(n):
            nums[i] //= n
        
        return nums