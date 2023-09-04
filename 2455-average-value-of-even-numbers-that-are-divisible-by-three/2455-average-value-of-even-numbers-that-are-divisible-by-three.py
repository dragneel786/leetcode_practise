class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = sums = 0
        for num in nums:
            if num % 3 == num % 2 == 0:
                count += 1
                sums += num
        return sums // count if count else 0