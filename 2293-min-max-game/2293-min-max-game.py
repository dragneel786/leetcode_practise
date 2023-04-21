class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while(len(nums) > 1):
            new_nums = []
            mini = True
            for i in range(0, len(nums) - 1, 2):
                if(mini):
                    new_nums.append(min(nums[i], nums[i + 1]))
                else:
                    new_nums.append(max(nums[i], nums[i + 1]))
                
                mini = not mini
            # break
            
            nums = new_nums
        
        return nums[0]