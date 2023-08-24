class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = count = 0
        for a, b in Counter([min(x, y) for x, y in rectangles]).items():
            if(a > max_len):
                count = b
                max_len = a
        
        return count