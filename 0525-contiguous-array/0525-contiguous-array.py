class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}
        count = ans = 0
        for i, num in enumerate(nums):
            count += 1 if(num == 1) else -1
            seen.setdefault(count, i)
            ans = max(ans, i - seen[count])
        
        return ans
            
            
            
        