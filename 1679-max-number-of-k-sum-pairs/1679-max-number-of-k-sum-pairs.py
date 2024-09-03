class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = pairs = 0
        end = len(nums) - 1
        while(start < end):
            val = nums[start] + nums[end]
            if val == k:
                pairs += 1
                start += 1
                end -= 1
            
            elif val > k:
                end -= 1
            
            else:
                start += 1
                
        
        return pairs
            
            
            