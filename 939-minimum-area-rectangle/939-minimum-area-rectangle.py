class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coord = set()
        for p in points:
            coord.add(tuple(p))
        
        minA = math.inf
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                area = abs(x1 - x2) * abs(y1 - y2)
                if(area and (minA > area) and (x1, y2) in coord and (x2, y1) in coord):
                    minA = area
                    
        return minA if(minA != math.inf) else 0
            
            
        