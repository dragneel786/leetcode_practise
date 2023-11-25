class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        curr = ans = 0
        while(curr < n):
            start = curr
            while(start < n and \
                  nums[curr] - nums[start] <= k):
                start += 1
            
            ans += 1
            curr = start
        
        return ans
            
            
            