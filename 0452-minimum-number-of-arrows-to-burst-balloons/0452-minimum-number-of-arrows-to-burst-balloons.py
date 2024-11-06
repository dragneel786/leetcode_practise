class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        counts = 1
        curr_end = points[0][1]
        for start, end in points:
            if start <= curr_end:
                continue
            
            curr_end = end
            counts += 1
        
        return counts
        
                