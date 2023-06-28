class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 1
        j = n - 2
        while(i < n):
            if(nums[i] != nums[i - 1]):
                break
            i += 1
            
        while(j > 0):
            if(nums[j] != nums[j + 1]):
                break
            j -= 1
        
        return 0 if(i > j) else j - i + 1
    