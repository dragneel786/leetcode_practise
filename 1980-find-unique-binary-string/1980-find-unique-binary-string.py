class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hset = set(nums)
        nums.sort()
        n = len(nums)
        start = '0' * n
        while(start in nums):
            val = int(start, 2)
            start = bin(val + 1)[2:]
            start = '0' * (n - len(start)) + start
        
        return start
            