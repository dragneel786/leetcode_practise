class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        def midL(idx):
            low = idx + 1
            high = n - 2
            res = -1
            while(low <= high):
                mid = (high - low) // 2 + low
                if(nums[idx] <= nums[mid] - nums[idx]):
                    if(nums[mid] - nums[idx] <= nums[-1] - nums[mid]):
                        res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res
        
        def midR(idx):
            low = idx + 1
            high = n - 2
            res = -1
            while(low <= high):
                mid = (high - low) // 2 + low
                if(nums[idx] <= nums[mid] - nums[idx]):
                    if(nums[mid] - nums[idx] <= nums[-1] - nums[mid]):
                        res = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    low = mid + 1
            return res
        
        count = 0
        for i in range(n - 2):
            left = midL(i)
            right = midR(i)
            if(left != -1 and right != -1):
                count += (right - left + 1)
         
        return count % ((10 ** 9) + 7)
            
            
    
        
        