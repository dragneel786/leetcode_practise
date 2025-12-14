class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        nums_with_refl = []
        for num in nums:
            val = 0
            temp = num
            while(num):
                val = (val << 1) | (num & 1)
                num >>= 1
            
            nums_with_refl.append((val, temp))
        
        return [val for _, val in sorted(nums_with_refl)]
