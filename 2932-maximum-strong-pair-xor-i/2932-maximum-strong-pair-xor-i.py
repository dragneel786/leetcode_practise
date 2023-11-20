class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        max_xor = 0
        for a in nums:
            for b in nums:
                if(abs(a - b) <= min(a, b)):
                    max_xor = max(max_xor, a ^ b)
            
        return max_xor