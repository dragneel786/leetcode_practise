class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = inf
        for num in nums:
            temp = 0
            while(num):
                temp += num % 10
                num //= 10
            
            min_val = min(min_val, temp)
        
        return min_val
        