class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd = even = 0
        for i, num in enumerate(nums):
            if(i & 1):
                odd += num
            else:
                even += num
        
        
        bodd = beven = count = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            to, te = bodd, beven
            if(i & 1):
                odd -= num
                bodd += num
            else:
                even -= num
                beven += num
            
            if(odd + te == even + to):
                count += 1
        
        return count
            
            
        
        