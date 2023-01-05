class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 0
        maxe = -inf
        for s, e in points:
            if(s > maxe):
                arrows += 1
                maxe = e
        
        return arrows