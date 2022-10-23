class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor_nums = 0
        counts = Counter(nums)
        repeat = 0
        
        for i, num in enumerate(nums, 1):
            xor_nums ^= (i ^ num)
            if(counts[num] == 2):
                repeat = num
        
        return [repeat, xor_nums ^ repeat]
        