class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        ans = j = 0
        for i, num in enumerate(nums):
            count[num] += 1
            while(count[num] > k):
                count[nums[j]] -= 1
                j += 1
            
            ans = max(i - j + 1, ans)
        
        return ans