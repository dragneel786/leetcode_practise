class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minv, maxv = arrays[0][0], arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            cmin, cmax = arrays[i][0], arrays[i][-1]
            res = max(res, abs(cmin-minv), abs(cmin-maxv),\
                      abs(cmax-maxv), abs(cmax-minv))
            minv, maxv = min(cmin, minv), max(cmax, maxv)
        
        return res
        