class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xored = 0
        for num in nums:
            xored ^= num
        
        kones = (1 << maximumBit) - 1
        res = []
        for i in range(len(nums) - 1, -1, -1):
            ans = 0
            for k in range(maximumBit):
                p = xored & (1 << k)
                ans += (not p) << k
            res.append(ans)
            xored ^= nums[i]
        
        return res
            
            
            
            
            