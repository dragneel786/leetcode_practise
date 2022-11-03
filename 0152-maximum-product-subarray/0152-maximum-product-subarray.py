class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = max_so_far
        
        for num in nums[1:]:
            val =  (max_so_far * num, min_so_far * num)
            max_so_far, min_so_far = max(num, *val), min(num, *val)
            
            ans = max(ans, max_so_far)
        
        return ans