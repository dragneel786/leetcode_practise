class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_value = inf
        max_value = -inf
        for num in nums:
            min_value = min(min_value, num)
            max_value = max(max_value, num)
        
        for g in range(min_value, 0, -1):
            div1, div2 = min_value % g, max_value % g
            if(not div1 and not div2):
                return g
        
        
            