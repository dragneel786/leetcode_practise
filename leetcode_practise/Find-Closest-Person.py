class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_x = abs(z - x)
        diff_y = abs(z - y)
        if diff_x < diff_y:
            return 1
        
        return 0 if diff_x == diff_y else 2