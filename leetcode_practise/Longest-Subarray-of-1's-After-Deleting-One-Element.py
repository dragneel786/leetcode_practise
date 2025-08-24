class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = zeros = start = 0
        for i, num in enumerate(nums):
            while(num == 0 and zeros > 0):
                zeros -= nums[start] == 0
                start += 1
            
            if num == 0:
                zeros += num == 0
            
            ans = max(ans, i - start)
            # print(i, start, zeros, ans)
        
        return ans
            

            


