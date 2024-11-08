class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        val = 0
        for num in nums:
            val ^= num
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            bit_shift = 1
            ith_res = 0
            for _ in range(maximumBit):
                if not (val & bit_shift):
                    ith_res |= bit_shift
                
                bit_shift <<= 1
                    
            res.append(ith_res)
            val ^= nums[i]
        
        return res
                    
            