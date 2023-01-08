class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxl = 1
        for i, (x1, y1) in enumerate(points[:-1]):
            has = defaultdict(lambda:0)
            for j, (x2, y2) in enumerate(points[i + 1:]):
                if(x2 == x1):
                    has[inf] += 1
                    maxl = max(maxl, has[inf] + 1)
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    has[slope] += 1
                    maxl = max(maxl, has[slope] + 1)
                
        return maxl