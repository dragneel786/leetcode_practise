class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return -max([sum(num % d == 0 for num in nums), -d] for d in divisors)[1]
                