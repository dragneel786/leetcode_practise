class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        is_same = lambda idx, ele: nums[idx] != ele
        in_first = lambda idx, ele: nums[idx] <= ele
        
        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = low + ((high - low) // 2)
            if(nums[mid] == target):
                return True
            
            if(not is_same(low, nums[mid])):
                low += 1
                continue
            
            pivot_array = in_first(low, nums[mid])
            target_array = in_first(low, target)
            
            if(pivot_array ^ target_array):
                if(pivot_array):
                    low = mid + 1
                else:
                    high = mid - 1
            
            else:
                if(nums[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False