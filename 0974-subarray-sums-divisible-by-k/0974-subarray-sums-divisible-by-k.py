class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = tot = 0
        remain = defaultdict(int)
        remain[0] = 1
        for num in nums:
            tot += num
            mod = tot % k
            ans += remain[mod]
            remain[mod] += 1
        
        return ans