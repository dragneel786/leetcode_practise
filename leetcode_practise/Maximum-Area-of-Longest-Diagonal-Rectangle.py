class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = max_area = 0
        for a, b in dimensions:
            dg = sqrt((a*a) + (b*b))
            if dg >= max_d:
                if max_d == dg:
                    max_area = max(max_area, a * b)
                else:
                    max_area = a * b
                
                max_d = dg

        return max_area


