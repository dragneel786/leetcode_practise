class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = c = 0
        for num in nums:
            if(not num):
                ans = max(c, ans)
                c = 0
            c += num
        
        return max(c, ans)