class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (high - low) // 2 + low
            
            if(nums[mid] == target):
                ans = mid
                break
            
            if(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
    
        return ans