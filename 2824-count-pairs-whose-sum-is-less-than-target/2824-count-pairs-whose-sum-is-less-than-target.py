class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot = 0
        for i in range(len(nums) - 1, 0, -1):
            j = i - 1
            while(j > -1 and nums[i] + nums[j] >= target):
                j -= 1
                
            if(j >= 0):
                tot += (j + 1)
        
        return tot
                