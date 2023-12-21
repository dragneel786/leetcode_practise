class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        x, y = points[0]
        ans = 0
        for a, b in points[1:]:
            ans = max(a - x, ans)
            x, y = a, b
        
        return ans
            