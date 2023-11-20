class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        max_xor = 0
        for i, a in enumerate(nums):
            for b in nums[i:]:
                if(abs(a - b) <= min(a, b)):
                    max_xor = max(max_xor, a ^ b)
            
        return max_xor