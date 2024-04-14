class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        xor_1 = 0 if(n % 2 == 0) else reduce(lambda a, b: a ^ b, nums1)
        xor_2 = 0 if(m % 2 == 0) else reduce(lambda a, b: a ^ b, nums2)
        
        return xor_1 ^ xor_2
            
            