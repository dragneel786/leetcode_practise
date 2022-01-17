class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxCount = 1
        for i in range(n):
            lookup = dict()
            count = 0
            for j in range(i + 1, n):
                x = (points[j][0] - points[i][0])
                y = (points[j][1] - points[i][1])
                if(x == 0):
                    slope = ()
                else:
                    slope = y / x
                lookup[slope] = lookup.get(slope, 1) + 1
                count = max(lookup[slope], count)

            maxCount = max(count, maxCount)
        return maxCount