class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        prev_x, _ = points[0]
        res = -inf
        for x, _ in points:
            res = max(res, x - prev_x)
            prev_x = x
        
        return res