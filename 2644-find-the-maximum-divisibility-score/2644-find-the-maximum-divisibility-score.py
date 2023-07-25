class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        count = -inf
        ans = min(divisors)
        for div in divisors:
            cc = 0
            for num in nums:
                cc += num % div == 0
            
            if(cc > count):
                count = cc
                ans = div
            elif(cc == count):
                ans = min(div, ans)
            
        return ans
                