class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd = even = 0
        for i, num in enumerate(nums):
            if(i & 1):
                odd += num
            else:
                even += num
        
        
        fo = fe = count = 0
        for i in range(n):
            if(i & 1):
                fo += nums[i]
                count += (odd + fe - fo + nums[i]) == (even + fo - fe)
            else:
                fe += nums[i]
                count += (odd + fe - fo) == (even + fo - fe + nums[i])
            
        
        return count
            
            
        
        