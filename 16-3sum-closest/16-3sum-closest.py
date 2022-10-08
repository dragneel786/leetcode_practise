class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = inf
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while(left < right):
                val = nums[i] + nums[left] + nums[right]
                
                if(abs(target - val) < abs(diff)):
                    diff = target - val
                
                if(val > target):
                    right -= 1
                else:
                    left += 1
            
            if(not diff):
                break
                    
        return target - diff
                