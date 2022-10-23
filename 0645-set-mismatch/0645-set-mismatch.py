class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor_nums = 0
        repeat = 0
        
        for i, num in enumerate(nums, 1):
            val = abs(num)
            if(nums[val - 1] < 0):
                repeat = val
            else:
                nums[val - 1] = (~(nums[val - 1]) + 1)
            
            xor_nums ^= (i ^ val)
            
        return [repeat, xor_nums ^ repeat]
        