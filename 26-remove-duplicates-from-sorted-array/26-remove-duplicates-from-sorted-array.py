class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        while(j < n):
            if(nums[j] <= nums[i]):
                j += 1
                continue
                
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1

        return i + 1