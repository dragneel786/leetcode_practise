class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sums = sum(nums)
        if sums - nums[0] <= nums[0] \
        or sums - nums[1] <= nums[1] \
        or sums - nums[2] <= nums[2]:
            return "none"

        names = ["equilateral", "isosceles", "scalene"]
        nums = set(nums)
        return names[len(nums) - 1]

