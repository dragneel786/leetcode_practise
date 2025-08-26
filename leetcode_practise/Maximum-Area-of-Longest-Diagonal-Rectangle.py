class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = res = 0
        for a, b in dimensions:
            curr_area = sqrt((a*a) + (b*b))
            if max_area <= curr_area:
                if max_area == curr_area: 
                    res = max(res, a * b)
                else:
                    res = a * b
                max_area = curr_area

        return res