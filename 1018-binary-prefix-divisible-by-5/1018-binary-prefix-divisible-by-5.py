class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        res = []
        for num in nums:
            val = (2 * val) + num
            res.append(val % 5 == 0)
        
        return res