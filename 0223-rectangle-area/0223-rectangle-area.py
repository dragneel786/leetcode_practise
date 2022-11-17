class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area = lambda x1, x2, y1, y2: max(x2 - x1, 0) * max(y2 - y1, 0)
        
        A = area(ax1, ax2, ay1, ay2)
        B = area(bx1, bx2, by1, by2)
        ox1 = max(ax1, bx1)
        ox2 = min(ax2, bx2)
        oy1 = max(ay1, by1)
        oy2 = min(ay2, by2)
        overlap = area(ox1, ox2, oy1, oy2)
        return A + B - overlap