class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def getMissingTill():
            return bisect_right(nums, mid)
        
        low = nums[0]
        high = nums[-1] + k
        while(low <= high):
            mid = ((high - low) >> 1) + low
            idx = getMissingTill()
            val = ((mid - nums[0]) + 1) - idx
            if(val == k and nums[idx - 1] != mid):
                return mid
            if(val < k):
                low = mid + 1
            else:
                high = mid - 1