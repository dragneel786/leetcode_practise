class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        left_tot, counts = 0, 0
        for i in range(len(nums) - 1):
            total -= nums[i]
            left_tot += nums[i]
            print(total, left_tot)
            counts += ((left_tot - total) % 2) == 0

        return counts