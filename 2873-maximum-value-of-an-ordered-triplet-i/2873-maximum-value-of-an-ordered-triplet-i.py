class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        val = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:], i + 1):
                for c in nums[j + 1:]:
                    comp = (a - b) * c
                    if(comp > val):
                        val = comp
        
        return val
                       
                    