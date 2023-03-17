class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = nums[0]
        counts = 0
        for i in range(1, len(nums) - 1):
            if(prev < nums[i] > nums[i + 1]):
                counts += 1
                prev = nums[i]
            
            elif(prev > nums[i] < nums[i + 1]):
                counts += 1
                prev = nums[i]
        
        return counts