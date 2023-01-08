class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxl = 1
        for i, (x1, y1) in enumerate(points):
            has = defaultdict(int)
            for j, (x2, y2) in enumerate(points):
                if(i != j):
                    val = atan2(x2 - x1, y2 - y1)
                    has[val] += 1
                    maxl = max(maxl, has[val] + 1)
        
        return maxl