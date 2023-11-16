class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        new_nums = [int(num, 2) for num in nums]
        n = len(nums)
        for i in range(1 << n):
            if(i not in new_nums):
                s = bin(i)[2:]
                val = '0' * (n - len(s)) + s
                return val
            