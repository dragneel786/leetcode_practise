class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for a in range(n - 1, -1, -1):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    val = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        ans += (val == nums[d])
                    
        return ans