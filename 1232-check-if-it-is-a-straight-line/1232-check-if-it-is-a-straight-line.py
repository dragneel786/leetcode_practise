class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        def slope(x1, y1, x2, y2):
            if(x1 - x2 == 0):
                return 0
            
            return (y1 - y2) / (x1 - x2)
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        for x3, y3 in coordinates[2:]:
            a = slope(x1, y1, x3, y3)
            b = slope(x2, y2, x3, y3)
            if(a != b):
                return False
        
        return True