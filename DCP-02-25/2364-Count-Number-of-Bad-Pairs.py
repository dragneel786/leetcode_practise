class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        tot = 0
        size = len(nums)
        pairs = Counter()
        for i, num in enumerate(nums):
            tot += (size - i - 1)
            pairs[i - num] += 1
        
        print(tot, pairs)
        for v in pairs.values():
            tot -= (v * (v - 1)) // 2
        
        return tot
        