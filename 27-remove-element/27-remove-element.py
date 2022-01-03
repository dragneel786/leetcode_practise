class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        idx = 0
        j = 0
        while(True):
            while(idx < n and nums[idx] != val):
                idx += 1
                j = idx + 1

            if(j >= n):
                break

            if(nums[j] != val and j > idx):
                nums[j], nums[idx] = nums[idx], nums[j]
            j += 1

        return (n - (n - idx))

        