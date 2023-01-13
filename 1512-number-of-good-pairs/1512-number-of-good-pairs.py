class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = Counter()
        ans = 0
        for num in nums:
            ans += seen[num]
            seen[num] += 1
        return ans
        