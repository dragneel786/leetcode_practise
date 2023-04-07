class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        ans = [0, 0]
        for v in counts.values():
            ans[0] += (v // 2)
            ans[1] += (v % 2)
        
        return ans