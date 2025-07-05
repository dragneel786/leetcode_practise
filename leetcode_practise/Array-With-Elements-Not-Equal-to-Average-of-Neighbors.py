class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        start = 0
        while(start < len(nums) // 2):
            res.append(nums[start])
            res.append(nums[len(nums) - start - 1])
            start += 1
        
        if len(nums) % 2 == 1:
            res.append(nums[start])
        return res