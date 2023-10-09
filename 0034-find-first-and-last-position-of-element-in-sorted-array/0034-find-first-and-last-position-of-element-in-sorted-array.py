class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def position_it(tar):
            low = 0
            high = len(nums)
            while(low < high):
                mid = low + ((high - low) // 2)
                if(nums[mid] < tar):
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        pos = position_it(target)
        if(pos >= len(nums) or nums[pos] != target):
            return [-1, -1]
        
        return [pos, position_it(target + 1) - 1]