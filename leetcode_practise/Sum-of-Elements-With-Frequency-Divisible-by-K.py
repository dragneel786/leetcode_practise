class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        tot = 0
        for key, freq in Counter(nums).items():
            if freq % k == 0:
                tot += (key * freq)
        
        return tot