class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        missing_count = lambda idx: nums[idx] - nums[0] - idx
        
        n = len(nums)
        if(k > missing_count(n - 1)):
            return nums[-1] + k - missing_count(n - 1)
        
        low, high = 0, n - 1
        while(low != high):
            pivot = ((high - low) >> 1) + low
            
            if(missing_count(pivot) < k):
                low = pivot + 1
            else:
                high = pivot
        
        return nums[low - 1] + k - missing_count(low - 1)