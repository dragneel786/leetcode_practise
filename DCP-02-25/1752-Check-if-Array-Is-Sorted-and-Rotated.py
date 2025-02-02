class Solution:
    def check(self, nums: List[int]) -> bool:
        dips = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                dips += 1

            if dips == 1 and nums[0] < nums[i + 1]:
                return False

            if dips > 1:
                return False
        
        return True