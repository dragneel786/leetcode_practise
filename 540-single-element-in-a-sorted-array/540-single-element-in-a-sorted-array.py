class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        if(n == 1):
            return nums[-1]
        high = n - 1
        while(low <= high):
            mid = (high - low) // 2 + low
            if((mid == n - 1 and nums[mid] != nums[mid - 1]) or\
              (mid == 0 and nums[mid + 1] != nums[mid])):
                return nums[mid]
            
            elif(nums[mid - 1] != nums[mid] != nums[mid + 1]):
                return nums[mid]
        
            if(nums[mid] == nums[mid - 1]):
                if(mid % 2 == 0):
                    high = mid
                else:
                    low = mid + 1
            elif(nums[mid] == nums[mid + 1]):
                if(mid % 2 == 0):
                    low = mid + 2
                else:
                    high = mid - 1
            
            