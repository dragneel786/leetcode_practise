class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = ans = 0
        for g in gain:
            curr += g
            ans = max(ans, curr)
        
        return ans