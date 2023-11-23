class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = 0
        for a in range(1, ceil(sqrt(area)) + 1):
            if(area % a == 0 and (area // a) >= a):
                l = area // a
                w = a
        
        return [l, w]