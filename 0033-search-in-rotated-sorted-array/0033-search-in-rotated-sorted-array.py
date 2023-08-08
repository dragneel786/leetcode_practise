class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_pivot():
            low = 0
            high = n - 1
            while(low <= high):
                mid = low + ((high - low) // 2)
                if(mid != 0 and nums[mid - 1] > nums[mid]):
                    return mid
                
                if(nums[0] > nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            
            return low
                    
        n = len(nums)
        idx = find_pivot()
        left = nums[:idx]
        right = nums[idx:]
    
        if(left):
            i = bisect_right(left, target)
            if(left[i - 1 if(i) else i] == target):
                return i - 1
        
        if(right):
            i = bisect_right(right, target)
            if(right[i - 1] == target):
                return idx + i - 1
        
        return -1