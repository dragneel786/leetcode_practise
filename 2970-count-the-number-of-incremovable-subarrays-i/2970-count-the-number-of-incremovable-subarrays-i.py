class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        def check_incre(arr, skip_start, skip_end):
            prev = 0
            for i in range(len(arr)):
                if(i >= skip_start and i < skip_end):
                    continue
                
                if(prev >= arr[i]):
                    return 0
                
                prev = arr[i]
                
            return 1
        
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                # print(nums[i:j + 1])
                ans += check_incre(nums, i, j + 1)
        
        return ans