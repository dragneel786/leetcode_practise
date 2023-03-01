class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(nums):
            n = len(nums)
            if(n > 1):
                left = divide(nums[:n // 2])
                right = divide(nums[n // 2:])
                return merge(left, right)
        
            return nums
        
        def merge(left, right):
            merged = []
            i = 0
            j = 0
            while(i < len(left) or j < len(right)):
                if(j >= len(right) or \
                    (i < len(left) and left[i] < right[j])):
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            return merged
        
        return divide(nums)