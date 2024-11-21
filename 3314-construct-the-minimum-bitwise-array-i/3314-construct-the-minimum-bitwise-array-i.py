class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            for a in range(num):
                if a | (a + 1) == num:
                    res.append(a)
                    break
            
            else:
                res.append(-1)
        
        return res
            
            