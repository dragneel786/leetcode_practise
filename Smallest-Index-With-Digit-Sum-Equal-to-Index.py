class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            temp = num
            tot = 0
            while(temp):
                tot += temp % 10
                temp //= 10
            
            if tot == i:
                return i
        
        return -1
