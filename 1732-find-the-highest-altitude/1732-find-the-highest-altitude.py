class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        val = 0
        ans = 0
        for g in gain:
            val += g
            ans = max(val, ans)
            
        return ans