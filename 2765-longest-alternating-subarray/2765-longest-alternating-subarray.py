class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        largest = -1
        count = 0
        d = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if(diff != 1 * d):
                if(diff == 1):
                    count = 0
                    d = 1
                else:
                    count = d = -1
            
            count += 1
            d *= -1
            if(count):
                largest = max(count + 1, largest)
        
        return largest
            
            