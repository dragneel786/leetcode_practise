class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        res = []
        for num in nums:
            val = (val << 1) + num
            res.append(val % 5 == 0)
        
        return res