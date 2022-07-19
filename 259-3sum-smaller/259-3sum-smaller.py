class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        counts = 0
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while(left < right):
                val = nums[left] + nums[right] + nums[i]
                if(val < target):
                    counts += right - left
                    left += 1
                else:
                    right -= 1
        return counts